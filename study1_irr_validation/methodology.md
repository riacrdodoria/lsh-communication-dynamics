# Inter-Rater Reliability (IRR) Protocol

**Project:** Validation of LLM-Assisted Coding for Cognitive Perturbations
**Version:** 1.0
**Date:** February 16, 2026

---

## 1. Introduction

This document outlines the protocol for the inter-rater reliability (IRR) analysis conducted to validate the use of a Large Language Model (LLM) as a second coder for identifying cognitive perturbations in team meeting transcripts. The objective is to ensure that the coding process is reliable, consistent, and grounded in the established theoretical framework.

## 2. Raters

-   **Coder 1 (Human):** A domain expert in team cognition and the theoretical framework of the study.
-   **Coder 2 (LLM):** A large language model (GPT-4), prompted with the same coding scheme and instructions as the human coder.

## 3. Coding Process

The coding process was conducted in four distinct steps:

### Step 1: Independent Coding

Both coders independently analyzed the transcripts of the 17 meetings from Study 1. The unit of analysis was the **second**, where each second of the meeting was classified as either containing a perturbation (`1`) or not (`0`).

-   **Human Coder:** The domain expert reviewed each transcript, marking the start and end times of all identified perturbation events.
-   **LLM Coder:** The LLM processed each transcript with a structured prompt that included the operational definitions of the perturbation categories and illustrative examples. The LLM returned a list of perturbation events with timestamps.

### Step 2: Data Aggregation

The annotations from both coders were compiled into a single dataset. Each row in this dataset represents one second of a meeting and includes:

-   `meeting`: The meeting identifier.
-   `second`: The timestamp of the second.
-   `llm_perturbation`: The LLM's coding (1 or 0).
-   `human_perturbation`: The human coder's coding (1 or 0).

### Step 3: Reliability Analysis

Inter-rater reliability was assessed using two primary metrics:

1.  **Cohen's Kappa (κ):** To measure the level of agreement between the two coders, correcting for agreement that might occur by chance. A Kappa value > 0.80 is considered "Almost Perfect Agreement."
2.  **Raw Agreement:** The percentage of seconds where both coders made the same judgment (either both coded as perturbation or both as non-perturbation).

The analysis was performed using standard statistical software.

### Step 4: Reconciliation and Finalization

To create a final, definitive log of perturbation events, a reconciliation process was established:

-   **Rule:** In all cases of disagreement between the human and LLM coder, the judgment of the **human coder was considered final**.
-   **Process:** A `final_perturbation` column was created, reflecting the human coder's decision in cases of disagreement.

This final, reconciled dataset serves as the ground truth for the main study's analyses.
