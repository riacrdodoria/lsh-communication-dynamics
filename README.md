# LSH Communication Dynamics - Replication Materials

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-pending-blue.svg)](https://osf.io/)

This repository contains all materials necessary to replicate the analyses reported in:

> [Authors]. (2026). [Title of the paper]. *[Journal Name]*. [Manuscript submitted for publication]

## Overview

This study introduces and validates the **Last-Speaker-Holds (LSH)** method, a representational innovation that enables the analysis of team communication dynamics using simple, start-time-only transcript data. Two validation studies demonstrate that:

1.  **Study 1:** Dynamic communication metrics can reliably identify cognitive perturbations in real-world team meetings (N=17 meetings from 2 startup teams).
2.  **Study 2:** The LSH method shows strong convergent validity (r = .87 to .95) with the standard method across diverse high-stakes contexts (N=16 surgical and submarine teams).

## Data Confidentiality and Synthetic Data

**IMPORTANT NOTICE:** Due to confidentiality agreements with the participating organizations, the original meeting transcripts and raw data cannot be shared publicly.

To support transparency and reproducibility, this repository provides **synthetic datasets** that are algorithmically generated to preserve the key statistical properties of the original data without exposing any confidential information.

> **The synthetic datasets are NOT intended to replicate the underlying speaker dynamics.** Instead, they reproduce the second-order statistical structure (distributional properties, temporal autocorrelation, and inter-method correlations) of the original metrics for the express purpose of methodological replication.

## Repository Structure

```
lsh-communication-dynamics/
│
├── README.md                          # This file
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
│
├── data/
│   └── synthetic/                     # Synthetic datasets for Studies 1 and 2
│       ├── study1_synthetic.csv       # Study 1: Perturbation analysis time-series
│       └── study2_synthetic.csv       # Study 2: Convergent validity time-series
│
├── scripts/                           # Core analysis scripts
│   ├── 01_build_lsh_timeseries.py     # Build LSH time-series from transcripts
│   └── generate_synthetic_data.py     # Generate synthetic datasets
│
├── study1_perturbation_protocol/      # Study 1: Content-based perturbation identification
│   ├── README.md                      # Overview of the LLM-assisted classification process
│   ├── protocol/
│   │   ├── perturbation_classification_protocol.md  # Theoretical protocol (5 types, decision rules)
│   │   └── prompt.md                  # Final versioned LLM prompt (v3.0)
│   ├── validation/
│   │   └── validation_script.py       # Script to audit and validate LLM output
│   └── example/
│       ├── README.md                  # Instructions for running the worked example
│       ├── synthetic_transcript_chunk.csv       # Synthetic input transcript
│       ├── expected_llm_output_table1.csv       # Expected output: event classification
│       └── expected_llm_output_table2.csv       # Expected output: time-series augmentation
│
├── docs/
│   └── method_overview.md             # LSH method overview
│
└── figures/                           # Publication figures
    └── ...
```

## Installation and Replication

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1.  Clone this repository:
    ```bash
    git clone [URL to this repository]
    cd lsh-communication-dynamics
    ```

2.  Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Re-generating Synthetic Data (Studies 1 and 2)

```bash
python scripts/generate_synthetic_data.py
```

### Replicating the Perturbation Classification Protocol (Study 1)

See [`study1_perturbation_protocol/README.md`](study1_perturbation_protocol/README.md) for a full walkthrough of the LLM-assisted classification process, including the prompt, validation script, and a worked synthetic example.

## Citation

If you use these materials in your research, please cite the associated paper:

```bibtex
@article{[anonymous]2026[anonymous],
  title={[Title of the paper]},
  author={[Authors]},
  journal={[Journal Name]},
  year={2026},
  note={Manuscript submitted for publication}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
