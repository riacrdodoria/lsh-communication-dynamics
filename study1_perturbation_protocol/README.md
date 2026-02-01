# Study 1: Content-Based Perturbation Identification Protocol

This directory contains the full, anonymized protocol used to identify perturbations in meeting transcripts for Study 1, as described in the main paper. This method relies on qualitative, content-based analysis, facilitated by a Large Language Model (LLM) following a rigorous, multi-step protocol.

## Repository Structure

```
study1_perturbation_protocol/
│
├── README.md                       # This file
│
├── protocol/
│   ├── perturbation_classification_protocol.md   # The detailed, 7-step qualitative protocol
│   └── prompt.md                     # The final, versioned prompt given to the LLM
│
├── validation/
│   └── validation_script.py          # Python script to audit and validate the LLM's output
│
└── example/
    ├── synthetic_transcript_chunk.csv # A synthetic (mock) input file
    └── expected_llm_output.csv        # The expected, correctly formatted output from the LLM
```

## The Protocol

The classification process is not a single prompt, but a systematic, human-in-the-loop workflow designed to ensure reliability and consistency. The core components are:

1.  **Classification Protocol (`protocol/`):** A detailed document outlining the theoretical definition of a "perturbation," the five specific perturbation types, and rules for handling boundary cases. This document was used to train the human annotators and refine the LLM prompt.

2.  **Final LLM Prompt (`protocol/prompt.md`):** The versioned, final prompt used for the analysis. It instructs the LLM to act as a research assistant and classify events based on the provided transcript segments, adhering strictly to the five defined perturbation types.

3.  **Validation Script (`validation/`):** A Python script used to automatically audit the LLM's output CSV. It checks for formatting errors, invalid perturbation types, and flags statistically unusual patterns (e.g., 100% perturbation rates, homogeneous types) for human review.

## Reproducibility

To replicate the classification process:

1.  **Review the `perturbation_classification_protocol.md`** to understand the theoretical framework.
2.  **Use the `prompt.md`** as the system prompt for an LLM (e.g., GPT-4, Claude 3).
3.  **Provide the `synthetic_transcript_chunk.csv`** as the input data for the LLM to process.
4.  **Run the `validation_script.py`** on the LLM's output to ensure it conforms to the required format and quality checks.

This multi-step process ensures that any classification, whether performed by a human or an LLM, is transparent, replicable, and auditable.
