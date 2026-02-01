> **Note:** This document has been revised (February 2026) to reflect methodological improvements implemented in response to peer review.

# LSH Method Overview (Revised)

## Introduction

The **Last-Speaker-Holds (LSH)** method is a representational innovation that enables the analysis of team communication dynamics using simple, start-time-only transcript data. This document provides a comprehensive overview of the method, its theoretical foundation, and practical implementation.

## The Problem: The Data Accessibility Gap

Traditional methods for calculating dynamic communication metrics require specialized, laboratory-grade data that includes precise timestamps for both the **start and end** of every utterance. This requirement has created a significant bottleneck, preventing researchers from analyzing the vast archives of real-world meeting data available from sources like:

- Zoom, Microsoft Teams, and Google Meet transcripts
- Call center logs
- Historical meeting records
- Public conversational datasets

These sources typically only provide timestamps for the **start** of each utterance, making them incompatible with existing analysis methods.

## The LSH Solution

The LSH method solves this problem by constructing a time-series representation that only requires start-time data. The key insight is simple but powerful:

> **In the absence of end-time information, assume that each speaker's state persists until the next speaker begins.**

This "last-speaker-holds" rule creates a continuous, 1Hz time-series representation that captures the essential dynamics of turn-taking and communication flow.

## Method Details (Revised Implementation)

### Input Requirements

The LSH method requires only:

1.  **Speaker ID** for each utterance
2.  **Start time** (in seconds) for each utterance
3.  **Total meeting duration** (optional, but recommended for accuracy)

### Construction Process

1.  **Sort utterances** by start time.
2.  **Create a 1Hz time-series** for the full duration of the meeting.
3.  **Assign speakers** using the last-speaker-holds rule:
    - From an utterance's start time until the second before the *next* utterance starts, assign the current speaker.
    - The final speaker holds their state until the end of the meeting.

### Output

A continuous time-series where each second is labeled with the active speaker. This series can then be encoded numerically and used to calculate dynamic metrics (Entropy, %DET, RMSE).

## Theoretical Foundation

The LSH method is grounded in the Joint Cognitive Systems (JCS) framework, which emphasizes the functional organization of joint activity. The method serves as a bridge between:

- **Observable communication** (who speaks when)
- **Latent cognitive organization** (coordination dynamics)

By focusing on the **sequence and timing of speaker transitions**, the LSH method captures the essential dynamics of team communication without requiring detailed information about utterance duration or overlapping speech.

## Validation

The LSH method has been validated through two complementary studies:

-   **Study 1 (Perturbation Identification):** Successfully identified cognitive perturbations in real-world startup meetings with high accuracy (94.1% success rate for Entropy).
-   **Study 2 (Convergent Validity):** Demonstrated strong convergent validity (r = .87 to .95) with the standard, high-fidelity method in high-stakes contexts.

## Methodological Revisions for Synthetic Data

To enhance the realism and robustness of the replication materials, the synthetic data generation process has been revised:

1.  **Episodic Perturbations:** Perturbations are now modeled as **contiguous blocks** of time, reflecting the episodic nature of real-world disruptions.
2.  **Stationary AR(1) Process:** Time-series are generated using a canonical, stationary AR(1) process to ensure they have the desired distributional properties without post-hoc manipulation.

## Implementation

See the following revised scripts for implementation details:

-   `scripts/01_build_lsh_timeseries.py`: Build LSH time-series from transcripts.
-   `scripts/generate_synthetic_data.py`: Generate methodologically robust synthetic data.

## References

[Authors]. (2025). [Title of the paper]. *Journal Name*. [Manuscript submitted for publication]

[Reference to related work].

---

**Last Updated:** February 20, 2026
