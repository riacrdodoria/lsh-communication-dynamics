#!/usr/bin/env python3.11
"""
Automated Validation Script for Perturbation Analysis (v2.0 - Alert System)
Version: 2.0
Date: February 9, 2026

Key changes from v1.0:
- Removed automatic rejection based on perturbation rate or count
- Changed to alert system: flags anomalies for manual review
- Added qualitative validation checks
- Focus on consistency and justification quality
"""

import pandas as pd
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class PerturbationValidator:
    """Validates perturbation analysis outputs for quality and consistency."""
    
    def __init__(self, csv_path: str, md_path: str = None):
        """
        Initialize validator with paths to analysis files.
        
        Args:
            csv_path: Path to table1_*_event_classification_en.csv
            md_path: Optional path to analysis_*.md file
        """
        self.csv_path = Path(csv_path)
        self.md_path = Path(md_path) if md_path else None
        self.df = pd.read_csv(csv_path)
        self.errors = []  # Critical errors that should reject the analysis
        self.warnings = []  # Anomalies that require manual review
        self.info = []  # Informational messages
        
    def count_perturbations(self) -> int:
        """Count total perturbations in CSV."""
        if 'perturbation_flag' in self.df.columns:
            flags = self.df['perturbation_flag'].astype(str).str.lower()
            return (flags == 'yes').sum() + (flags == '1').sum() + (flags == 'true').sum()
        elif 'Perturbation_Flag' in self.df.columns:
            flags = self.df['Perturbation_Flag'].astype(str).str.lower()
            return (flags == 'yes').sum() + (flags == '1').sum() + (flags == 'true').sum()
        else:
            self.errors.append("ERROR: No perturbation_flag column found in CSV")
            return 0
    
    def validate_required_columns(self) -> bool:
        """Check if all required columns are present."""
        required = ['episode_id', 'event_id', 'perturbation_flag']
        missing = [col for col in required if col not in self.df.columns]
        
        if missing:
            self.errors.append(
                f"ERROR: Missing required columns: {missing}"
            )
            return False
        
        return True
    
    def validate_perturbation_rate(self) -> bool:
        """Alert on unusual perturbation rates (but don't reject)."""
        total_events = len(self.df)
        perturbations = self.count_perturbations()
        
        if total_events == 0:
            self.errors.append("ERROR: No events found in CSV")
            return False
        
        rate = (perturbations / total_events) * 100
        
        # Alert on extreme rates
        if rate == 100.0 and total_events > 10:
            self.warnings.append(
                f"⚠️  UNUSUAL: 100% perturbation rate ({perturbations}/{total_events}). "
                "This is statistically rare. Please manually review a sample of classifications "
                "to ensure they are genuine perturbations and not normal discussion."
            )
        elif rate > 60.0:
            self.warnings.append(
                f"⚠️  HIGH RATE: {rate:.1f}% perturbation rate ({perturbations}/{total_events}). "
                "This is higher than typical. If the meeting was a crisis or major pivot, this may be correct. "
                "Please manually review a sample to verify quality."
            )
        elif rate > 40.0:
            self.warnings.append(
                f"⚠️  ELEVATED RATE: {rate:.1f}% perturbation rate ({perturbations}/{total_events}). "
                "This is above average but may be legitimate. Spot-check a few classifications."
            )
        
        if perturbations == 0 and total_events > 20:
            self.warnings.append(
                f"⚠️  ZERO PERTURBATIONS: Found 0 perturbations in {total_events} events. "
                "This is unusual for a typical meeting. Please verify the analysis was completed correctly."
            )
        elif perturbations < 5 and total_events > 50:
            self.info.append(
                f"ℹ️  LOW COUNT: Only {perturbations} perturbations in {total_events} events. "
                "This may indicate a very smooth meeting or possible under-flagging."
            )
        
        return True
    
    def validate_type_distribution(self) -> bool:
        """Check if perturbation types are properly distributed."""
        if 'perturbation_type' not in self.df.columns and 'Perturbation_Type' not in self.df.columns:
            self.warnings.append("⚠️  WARNING: No perturbation_type column found")
            return True
        
        type_col = 'perturbation_type' if 'perturbation_type' in self.df.columns else 'Perturbation_Type'
        
        # Get perturbations only
        flag_col = 'perturbation_flag' if 'perturbation_flag' in self.df.columns else 'Perturbation_Flag'
        pert_df = self.df[self.df[flag_col].astype(str).str.lower().isin(['yes', '1', 'true'])]
        
        if len(pert_df) == 0:
            return True
        
        type_counts = pert_df[type_col].value_counts()
        
        # Check for invalid types
        valid_types = ['0', '1', '2', '3', '4', '5', 0, 1, 2, 3, 4, 5, '1; 2', '2; 3', '3; 4', '4; 5', '1; 5', '2; 5']
        invalid_types = [t for t in type_counts.index if t not in valid_types and not pd.isna(t)]
        if invalid_types:
            self.errors.append(
                f"ERROR: Invalid perturbation types found: {invalid_types}. "
                "Valid types are 1-5 (or combinations like '2; 5')."
            )
            return False
        
        # Alert if all perturbations are of one type
        if len(type_counts) == 1 and len(pert_df) > 10:
            dominant_type = type_counts.index[0]
            self.warnings.append(
                f"⚠️  HOMOGENEOUS TYPES: All {len(pert_df)} perturbations are Type {dominant_type}. "
                "While this is possible, it's unusual. Please verify this reflects the actual meeting dynamics."
            )
        
        # Alert if one type dominates heavily
        if len(type_counts) > 1:
            max_type = type_counts.iloc[0]
            total = type_counts.sum()
            if max_type / total > 0.8 and total > 10:
                self.warnings.append(
                    f"⚠️  DOMINANT TYPE: {max_type}/{total} ({max_type/total*100:.0f}%) perturbations are of one type. "
                    "This may be legitimate, but please verify diversity of classifications."
                )
        
        return True
    
    def validate_text_csv_consistency(self) -> bool:
        """Check if markdown text matches CSV counts (if md_path provided)."""
        if not self.md_path or not self.md_path.exists():
            self.info.append("ℹ️  No markdown file provided for text-CSV consistency check")
            return True
        
        try:
            with open(self.md_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract total from text
            import re
            total_match = re.search(r'[Tt]otal.*?[Pp]erturbations.*?(\d+)', content)
            
            if total_match:
                text_count = int(total_match.group(1))
                csv_count = self.count_perturbations()
                
                if text_count != csv_count:
                    self.errors.append(
                        f"ERROR: Text-CSV mismatch. "
                        f"Markdown reports {text_count} perturbations, "
                        f"but CSV has {csv_count}. These MUST match."
                    )
                    return False
                else:
                    self.info.append(f"✓ Text-CSV consistency verified: {text_count} perturbations")
            else:
                self.warnings.append("⚠️  Could not extract perturbation count from markdown for verification")
        except Exception as e:
            self.warnings.append(f"⚠️  Could not validate text-CSV consistency: {e}")
        
        return True
    
    def validate_justifications(self) -> bool:
        """Check if perturbations have justifications (qualitative check)."""
        flag_col = 'perturbation_flag' if 'perturbation_flag' in self.df.columns else 'Perturbation_Flag'
        desc_col = 'event_description' if 'event_description' in self.df.columns else None
        
        if desc_col is None:
            self.warnings.append("⚠️  No event_description column found. Cannot verify justifications.")
            return True
        
        pert_df = self.df[self.df[flag_col].astype(str).str.lower().isin(['yes', '1', 'true'])]
        
        if len(pert_df) == 0:
            return True
        
        # Check for empty or very short descriptions
        empty_descriptions = pert_df[desc_col].isna().sum()
        short_descriptions = (pert_df[desc_col].astype(str).str.len() < 20).sum()
        
        if empty_descriptions > 0:
            self.warnings.append(
                f"⚠️  MISSING JUSTIFICATIONS: {empty_descriptions}/{len(pert_df)} perturbations "
                "have no description/justification. Each perturbation should be justified."
            )
        
        if short_descriptions > len(pert_df) * 0.5:
            self.warnings.append(
                f"⚠️  WEAK JUSTIFICATIONS: {short_descriptions}/{len(pert_df)} perturbations "
                "have very short descriptions (<20 chars). Justifications should include textual evidence."
            )
        
        return True
    
    def validate_episode_structure(self) -> bool:
        """Check if episodes were properly created."""
        if 'episode_id' not in self.df.columns:
            return True
        
        unique_episodes = self.df['episode_id'].nunique()
        total_events = len(self.df)
        
        if unique_episodes == 1 and total_events > 20:
            self.warnings.append(
                f"⚠️  FLAT STRUCTURE: Only 1 episode for {total_events} events. "
                "The transcript should be segmented into multiple coherent episodes."
            )
        elif unique_episodes == total_events:
            self.warnings.append(
                f"⚠️  OVER-SEGMENTATION: Each event is in its own episode ({unique_episodes} episodes). "
                "Episodes should group related events into coherent segments."
            )
        else:
            self.info.append(f"✓ Episode structure: {unique_episodes} episodes for {total_events} events")
        
        return True
    
    def run_all_validations(self) -> Tuple[bool, List[str], List[str], List[str]]:
        """
        Run all validation checks.
        
        Returns:
            Tuple of (passed, errors, warnings, info)
        """
        checks = [
            self.validate_required_columns(),
            self.validate_perturbation_rate(),
            self.validate_type_distribution(),
            self.validate_text_csv_consistency(),
            self.validate_justifications(),
            self.validate_episode_structure(),
        ]
        
        # Only fail if there are critical errors
        passed = all(checks) and len(self.errors) == 0
        return passed, self.errors, self.warnings, self.info
    
    def print_report(self):
        """Print validation report to console."""
        passed, errors, warnings, info = self.run_all_validations()
        
        print(f"\n{'='*80}")
        print(f"VALIDATION REPORT: {self.csv_path.name}")
        print(f"{'='*80}\n")
        
        total_events = len(self.df)
        perturbations = self.count_perturbations()
        rate = (perturbations / total_events * 100) if total_events > 0 else 0
        
        print(f"📊 STATISTICS:")
        print(f"   Total Events: {total_events}")
        print(f"   Perturbations: {perturbations}")
        print(f"   Perturbation Rate: {rate:.1f}%")
        print()
        
        if errors:
            print(f"❌ CRITICAL ERRORS ({len(errors)}) - ANALYSIS REJECTED:")
            for error in errors:
                print(f"   • {error}")
            print()
        
        if warnings:
            print(f"⚠️  WARNINGS ({len(warnings)}) - MANUAL REVIEW REQUIRED:")
            for warning in warnings:
                print(f"   • {warning}")
            print()
        
        if info:
            print(f"ℹ️  INFORMATION ({len(info)}):")
            for i in info:
                print(f"   • {i}")
            print()
        
        if passed and not warnings:
            print("✅ ALL CHECKS PASSED - ANALYSIS ACCEPTED")
        elif passed:
            print("⚠️  PASSED WITH WARNINGS - MANUAL REVIEW RECOMMENDED")
            print("    Review a sample of perturbations to verify quality before accepting.")
        else:
            print("❌ VALIDATION FAILED - ANALYSIS REJECTED")
            print("    Fix the critical errors and resubmit.")
        
        print(f"\n{'='*80}\n")
        
        return passed


def validate_directory(directory: str) -> Dict[str, str]:
    """
    Validate all CSV files in a directory.
    
    Args:
        directory: Path to directory containing CSV files
        
    Returns:
        Dictionary mapping filenames to status (passed/warnings/failed)
    """
    results = {}
    csv_files = list(Path(directory).glob('table1_*_event_classification_en.csv'))
    
    print(f"\n{'='*80}")
    print(f"BATCH VALIDATION: {len(csv_files)} files in {directory}")
    print(f"{'='*80}\n")
    
    for csv_file in csv_files:
        # Try to find corresponding markdown file
        meeting_name = csv_file.stem.replace('table1_', '').replace('_event_classification_en', '')
        md_file = csv_file.parent / f'analysis_{meeting_name}_en.md'
        
        validator = PerturbationValidator(
            str(csv_file),
            str(md_file) if md_file.exists() else None
        )
        
        passed, errors, warnings, info = validator.run_all_validations()
        
        if not passed:
            results[csv_file.name] = "FAILED"
        elif warnings:
            results[csv_file.name] = "WARNINGS"
        else:
            results[csv_file.name] = "PASSED"
    
    # Summary
    total = len(results)
    passed_count = sum(1 for v in results.values() if v == "PASSED")
    warnings_count = sum(1 for v in results.values() if v == "WARNINGS")
    failed_count = sum(1 for v in results.values() if v == "FAILED")
    
    print(f"\n{'='*80}")
    print(f"BATCH SUMMARY:")
    print(f"   ✅ Passed: {passed_count}/{total}")
    print(f"   ⚠️  Warnings: {warnings_count}/{total}")
    print(f"   ❌ Failed: {failed_count}/{total}")
    print(f"{'='*80}\n")
    
    if failed_count > 0:
        print(f"❌ {failed_count} files FAILED validation:")
        for filename, status in results.items():
            if status == "FAILED":
                print(f"   • {filename}")
        print()
    
    if warnings_count > 0:
        print(f"⚠️  {warnings_count} files have WARNINGS (manual review recommended):")
        for filename, status in results.items():
            if status == "WARNINGS":
                print(f"   • {filename}")
        print()
    
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Validate single file: python validation_script_v2_alerts.py <csv_file> [md_file]")
        print("  Validate directory:   python validation_script_v2_alerts.py <directory>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    
    if path.is_dir():
        # Validate entire directory
        results = validate_directory(str(path))
        # Exit with error only if there are failures
        sys.exit(0 if all(v != "FAILED" for v in results.values()) else 1)
    else:
        # Validate single file
        md_path = sys.argv[2] if len(sys.argv) > 2 else None
        validator = PerturbationValidator(str(path), md_path)
        passed = validator.print_report()
        sys.exit(0 if passed else 1)
