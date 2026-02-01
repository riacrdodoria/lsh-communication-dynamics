# Example: Synthetic Input and Expected LLM Output

This directory contains a worked example to demonstrate the full input-output cycle of the perturbation classification protocol. All data here is **entirely synthetic and fictional**. No real participant data is present.

## Files

| File | Description |
| :--- | :--- |
| `synthetic_transcript_chunk.csv` | A mock transcript segment in the format accepted by the protocol. Contains fictional speakers (Speaker_A, B, C) and fabricated utterances designed to illustrate all five perturbation types. |
| `expected_llm_output_table1.csv` | The expected **Table 1 — Event Classification** output from the LLM after processing the synthetic transcript. |
| `expected_llm_output_table2.csv` | The expected **Table 2 — Time Series Augmentation** output, mapping each utterance to its classified episode and event. |

## How to Use

1.  Open `protocol/prompt.md` and use it as the system prompt for your LLM of choice (e.g., GPT-4, Claude 3 Sonnet or higher).
2.  Provide the contents of `synthetic_transcript_chunk.csv` as the user message / input data.
3.  The LLM should produce outputs that match the structure of `expected_llm_output_table1.csv` and `expected_llm_output_table2.csv`.
4.  Run `validation/validation_script.py` on the LLM's Table 1 output to verify its quality.

## Perturbation Types Illustrated

The synthetic transcript is designed to contain one instance of each perturbation type:

| Type | Name | Illustrated By |
| :--- | :--- | :--- |
| **1** | Unexpected outcome or failure | Supplier proposal 40% over budget; user testing failure rate exceeds threshold |
| **2** | New risk or threat | Regulatory approval suspended by a new, previously unknown policy |
| **3** | Loss of shared understanding | Speaker C unsure whether the cost figure refers to unit cost or total contract value |
| **4** | Constraint or blockage | Team cannot proceed with pilot without the regulatory approval |
| **5** | Forced reprioritization | Team must formally abandon Q3 target and pivot to Q4 |
