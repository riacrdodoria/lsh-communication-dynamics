"""
Build LSH Time-Series from Transcripts (Publication-Ready)

This script demonstrates how to build a Last-Speaker-Holds (LSH) time-series
representation from simple start-time-only transcript data. This version has
been revised for methodological rigor and clarity, addressing feedback for
scientific publication.

Author: [Authors of the manuscript]
Date: February 2026 (Revised)
"""

import pandas as pd
import numpy as np
from typing import Optional

def build_lsh_timeseries(transcript_df: pd.DataFrame, 
                         sampling_rate: int = 1, 
                         meeting_duration: Optional[int] = None) -> pd.DataFrame:
    """
    Build LSH time-series from a transcript with start-time-only data.

    The LSH method assumes that communicative state persists until a new speaker
    initiates speech. Silence is therefore not modeled as an independent state,
    but as a temporal extension of the prior speaker's state. This approach is
    grounded in the principle that a speaker's influence on the cognitive system
    continues until another speaker takes the floor.

    Parameters:
    -----------
    transcript_df : pd.DataFrame
        Transcript with columns: ['speaker_id', 'start_time'].
        'start_time' should be in seconds.
        
    sampling_rate : int, optional
        Sampling rate in Hz (default: 1). For LSH based on start-times only,
        a 1Hz sampling rate is the most methodologically consistent choice.
        
    meeting_duration : int, optional
        The total duration of the meeting in seconds. If None (default), the
        time series will end at the start time of the final utterance.

    Returns:
    --------
    timeseries : pd.DataFrame
        A 1Hz time-series with columns: ['second', 'speaker_id'].

    Raises:
    -------
    ValueError:
        If the input DataFrame is empty or if start times are not unique and
        monotonically increasing.
    """
    if transcript_df.empty:
        raise ValueError("Input transcript_df cannot be empty.")

    # --- Methodological Check 1: Validate input data structure ---
    # Sort by start time and reset index to ensure proper alignment
    transcript_df = transcript_df.sort_values('start_time').reset_index(drop=True)

    # Ensure start times are unique and monotonically increasing to avoid ambiguity
    if not transcript_df['start_time'].is_unique:
        raise ValueError("Duplicate start_time values found. Each utterance must have a unique start time.")
    if not transcript_df['start_time'].is_monotonic_increasing:
        raise ValueError("start_time values must be monotonically increasing after sorting.")

    # --- Methodological Check 2: Determine total duration without artificial buffers ---
    if meeting_duration is None:
        # Default behavior: end series at the start of the last utterance.
        # Add 1 to ensure the final second is included in the range.
        max_time = int(transcript_df['start_time'].max()) + 1
    else:
        max_time = int(meeting_duration)

    # Initialize time-series DataFrame
    timeseries = pd.DataFrame({
        'second': np.arange(0, max_time, 1 / sampling_rate)
    })
    timeseries['speaker_id'] = None # Initialize with no speaker

    # --- Core LSH Algorithm: Assign speakers using a forward-fill logic ---
    for idx, row in transcript_df.iterrows():
        start_idx = int(row['start_time'] * sampling_rate)

        # Determine the end index for this speaker's hold period
        if idx < len(transcript_df) - 1:
            # The speaker holds until the second before the next speaker starts
            end_idx = int(transcript_df.loc[idx + 1, 'start_time'] * sampling_rate)
        else:
            # The last speaker holds until the end of the defined meeting duration
            end_idx = len(timeseries)

        # Assign the speaker to all seconds in the calculated interval.
        # Using .loc is efficient for this block-assignment task.
        timeseries.loc[start_idx:end_idx-1, 'speaker_id'] = row['speaker_id']

    # --- Finalization: Handle silence at the beginning of the meeting ---
    # Any remaining None values at the start of the series are explicitly labeled as 'SILENCE'.
    timeseries['speaker_id'].fillna('SILENCE', inplace=True)

    return timeseries

def encode_speakers_numeric(timeseries: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Encode speaker IDs as numeric values for metric calculation.

    Parameters:
    -----------
    timeseries : pd.DataFrame
        Time-series with a 'speaker_id' column.

    Returns:
    --------
    tuple[pd.DataFrame, dict]:
        - The time-series DataFrame with an added 'speaker_numeric' column.
        - A dictionary mapping original speaker IDs to their numeric codes.
    """
    # Create a mapping from unique speaker IDs to integer codes
    unique_speakers = timeseries['speaker_id'].unique()
    speaker_map = {speaker: idx for idx, speaker in enumerate(unique_speakers)}

    # Apply the mapping to create the numeric representation
    timeseries['speaker_numeric'] = timeseries['speaker_id'].map(speaker_map)

    return timeseries, speaker_map

def example_usage():
    """
    Example demonstrating the revised LSH time-series construction.
    """
    print("=" * 70)
    print("Revised LSH Time-Series Construction Example (Publication-Ready)")
    print("=" * 70)

    # Example transcript (start-time-only)
    transcript = pd.DataFrame({
        'speaker_id': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'],
        'start_time': [0, 5, 12, 18, 25, 30]
    })

    print("\n1. Input Transcript (start-time-only):")
    print(transcript)

    # --- Build LSH time-series using the revised, buffer-free method ---
    # We'll set a meeting_duration for a realistic scenario.
    # Let's assume the meeting was known to be 40 seconds long.
    meeting_end_time = 40
    timeseries = build_lsh_timeseries(transcript, meeting_duration=meeting_end_time)

    print(f"\n2. LSH Time-Series (Meeting Duration: {meeting_end_time}s):")
    print(timeseries)

    # --- Encode speakers numerically for analysis ---
    timeseries, speaker_map = encode_speakers_numeric(timeseries)

    print("\n3. Speaker Encoding Map:")
    for speaker, code in speaker_map.items():
        print(f"    {speaker}: {code}")

    print("\n4. Final Numeric Time-Series:")
    print(timeseries[['second', 'speaker_id', 'speaker_numeric']])

    print("\n\u2713 LSH time-series successfully constructed with methodological rigor!")
    print(f"  Total duration: {len(timeseries)} seconds")
    print(f"  Unique speakers (incl. SILENCE): {len(speaker_map)}")

    return timeseries

if __name__ == "__main__":
    # Run the demonstration example
    timeseries_example = example_usage()

    # This script is for demonstration; by default, it does not overwrite repository data.
    # To save the output, you can uncomment the following lines:
    # print("\nSaving example output to 'example_lsh_timeseries.csv'...")
    # timeseries_example.to_csv('../data/synthetic/example_lsh_timeseries.csv', index=False)
    # print("\u2713 Example saved.")
