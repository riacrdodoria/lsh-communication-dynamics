># Content-Based Perturbation Classification Protocol

**Author**: Manus AI  
**Date**: January 22, 2026  
**Version**: 1.0

---

## 1. Introduction

This document establishes a formal protocol for the qualitative, theory-driven content analysis of team meeting transcripts. The primary objective is to **identify and flag perturbations** that occur during the interaction, based exclusively on the semantic content of the dialogue. This method aims to provide a systematic and replicable approach to understanding how teams handle disruptions in the flow of their collective activities, avoiding the inference of perturbations from quantitative metrics such as talk time, pauses, or volume.

## 2. Operational Definition of Perturbation

For the purposes of this protocol, a **perturbation** is defined as a disruption in the expected flow of collective activity that requires the team to reassess the situation, reconsider plans, or reorganize action. A perturbation represents a moment when smooth progress is broken, forcing the team into a problem-solving or reorientation mode.

A an event must only be flagged as a perturbation if it involves at least one of the following five categories:

| Type | Perturbation Category | Description |
| :--- | :--- | :--- |
| 1 | **Emergence of an unexpected outcome or failure** | The result of an action or event deviates significantly from what was expected, including explicit failures to achieve a goal. |
| 2 | **Emergence of a new risk or threat** | A new threat, risk, or significant concern is identified and verbalized, with the potential to negatively impact the project or team. |
| 3 | **Explicit loss of shared understanding** | A clear breakdown in mutual understanding occurs, where team members realize they are operating based on different assumptions or information. |
| 4 | **Constraint or blockage that prevents planned action** | A barrier, constraint, or concrete obstacle prevents the team from executing an action that had been planned. |
| 5 | **Forced reprioritization or abandonment of a plan** | The team is forced to abandon a planned course of action or drastically change its priorities in response to new information or circumstances. |

## 3. Decision Rules

The analysis process must follow a structured approach to ensure consistency.

1.  **Transcript Segmentation**: The transcript must be read sequentially and segmented into two levels:
    *   **Episodes (meso-level)**: Represent a coherent segment of the interaction, usually focused on a single topic or activity (e.g., "Scorecard Review," "Discussion about Partnership X").
    *   **Events (micro-level)**: Occur within episodes and represent specific moments of decision, information revelation, or change in the flow of conversation.

2.  **Perturbation Flagging**: An event should only be flagged (`perturbation_flag = 'yes'`) if the semantic content of the interaction explicitly meets one or more of the five perturbation types defined in Section 2. The decision must be justified based on direct textual cues (quotes from the transcript).

3.  **Exclusive Focus on Content**: The analysis must strictly ignore any non-semantic cues. Perturbations should not be inferred based on:
    *   Duration of pauses or silences.
    *   Tone of voice, intensity, or overlapping speech (unless the content of the speech comments on the interruption).
    *   Prior knowledge of project outcomes.
    *   Frequency of speaker turnover.

## 4. Boundary Cases and How to Handle Them

The distinction between a perturbation and the normal dynamics of a meeting can be subtle. The following table addresses common boundary cases.

| Scenario | Is it a Perturbation? | Justification and Decision Rule |
| :--- | :--- | :--- |
| **Routine Adjustment vs. Forced Reorganization** | **NO** | Flexible adjustments to the agenda or plan that are not caused by a failure or blockage are not perturbations. Ex: Changing the order of topics because a participant is late. |
| **Debate or Disagreement vs. Loss of Understanding** | **NO** | A healthy debate or disagreement about the best way to proceed is not a perturbation. It becomes a perturbation (Type 3) only when there is explicit evidence that participants are not understanding each other. |
| **Discussion of Future Risks vs. Emergence of New Risk** | **NO** | Proactive planning and discussion of potential future risks are not perturbations. It becomes a perturbation (Type 2) when a *new and immediate* risk is verbalized for the first time, causing concern. |
| **Slow Progress vs. Blockage** | **NO** | Slower-than-desired progress on a task is not, in itself, a perturbation. It becomes a perturbation (Type 4) when the team verbalizes that it is *prevented* from moving forward due to a concrete obstacle. |

## 5. Examples of Perturbations and Non-Perturbations

The table below provides concrete examples from the pilot analyses to illustrate the application of the protocol.

| Example | Classification | Type | Justification |
| :--- | :--- | :--- | :--- |
| "*we are in a bureaucracy within a large corporation. To enable the paid version of IX...*" | **Perturbation** | 4 | An external constraint (bureaucracy) is preventing a planned action (implementing payment). |
| "*Searching and we didn't find, and what we found, they didn't want.*" | **Perturbation** | 1 | The result of an action (searching for batteries) was an unexpected failure. |
| "*This will always be a problem, right.*" (about customer loyalty) | **Perturbation** | 2 | The team verbalizes a structural and ongoing risk to their business model. |
| "*we also kind of left aside doing a Press Release because we are already well aligned with them...*" | **Perturbation** | 5 | A planned action (Press Release) is explicitly abandoned in favor of another approach. |
| "*it can't be 100 reais, right? Isn't a diagnosis more expensive?*" | **Perturbation** | 3 | Demonstrates a clear loss of understanding about what the R$100 value represented (profit vs. cost). |
| "*We can take a look at a partner because I think they will be late.*" | **Non-Perturbation** | N/A | A flexible and proactive agenda adjustment, not a forced reorganization. |
| "*We presented our idea to them, they... liked the idea a lot...*" | **Non-Perturbation** | N/A | Represents the normal and expected progress in a negotiation with a partner. |

## 6. Limitations of Content-Based Inference

It is crucial to recognize the inherent limitations of this method:

*   **Interpretive Subjectivity**: Although the protocol aims for objectivity, the qualitative analysis of text still contains an element of interpretation that may vary between different analysts.
*   **Omission of Non-Verbal Cues**: The method is blind to crucial dynamics communicated through tone of voice, body language, and other non-verbal cues that may signal perturbations.
*   **Dependence on Explicitness**: The protocol can only capture perturbations that are explicitly verbalized by the team. Problems that remain implicit or unsaid will not be identified.
*   **Lack of Full Context**: The analysis is performed without the full context of the project, the organization, and interpersonal relationships, which may lead to misinterpretations of certain events.

## 7. Output Structure

To ensure data consistency for future analyses, the results must be presented in two table formats:

1.  **Table 1 — Event Classification**: A summary of all identified events, with columns for `episode_id`, `episode_name`, `event_id`, `event_name`, `level`, `perturbation_flag`, `perturbation_type`, `episode_description`, and `event_description`.
2.  **Table 2 — Time Series Augmentation**: The original transcript CSV file (1hz format), augmented with the columns `episode_id`, `episode_name`, `event_id`, `event_name`, `level`, and `perturbation_flag`, to allow for temporal analysis of perturbations.
