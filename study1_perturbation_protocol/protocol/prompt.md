# Improved Prompt for Perturbation Analysis (v3.0 - No Quantitative Limits)

**Version:** 3.0  
**Date:** February 9, 2026  
**Key Change:** Removed artificial quantitative limits; focus on qualitative classification quality

---

## Core Instructions

You are analyzing a team meeting transcript to identify **perturbations** — disruptions in the expected flow of team activity that force the team to stop, reassess, reconsider, or reorganize their approach.

**Important principles:**
- **Perturbations are exceptions, not the rule.** Most discussion is normal progress.
- **However, some meetings may genuinely have many perturbations** (e.g., during crises, major pivots, or high-uncertainty periods). Do not suppress real data.
- **Your job is to identify ALL genuine perturbations, regardless of how many there are.**
- **Quality over quantity:** Each perturbation must have clear textual evidence and fit one of the five types.

---

## Definition of Perturbation

A **perturbation** is a disruption in the expected flow of collective activity that requires the team to:
- **Reassess** the situation
- **Reconsider** their plans
- **Reorganize** their actions

It represents a moment when smooth progress breaks down and the team must engage in problem-solving or reorientation.

---

## The Five Perturbation Types

Every perturbation must fit into **exactly one** of these five categories:

| Type | Name | Operational Definition | Key Textual Cues |
|:---|:---|:---|:---|
| **1** | Unexpected outcome or failure | An action's result deviates significantly from expectations, or an explicit failure occurs | "We expected X but got Y", "It didn't work", "We failed to..." |
| **2** | New risk or threat | A new, immediate threat/risk is verbalized for the first time, causing concern | "We just learned that...", "A new competitor...", "Regulation changed..." |
| **3** | Loss of shared understanding | Team members realize they're operating on different assumptions or information | "Wait, I thought we agreed on X", "I'm confused about...", "Which one is it?" |
| **4** | Constraint or blockage | A concrete obstacle **prevents** planned action (not just slows it) | "We can't do X because...", "We're blocked by...", "We don't have access to..." |
| **5** | Forced reprioritization | Team **must abandon** or drastically change a planned course of action | "We have to drop X", "Given Y, we must pivot to...", "We can no longer..." |

---

## What IS a Perturbation: Examples with Justifications

### Type 1: Unexpected Outcome or Failure
✅ "We tested the prototype with 5 users and all of them abandoned it within 2 minutes. We expected at least 50% completion."
- **Why:** Explicit unexpected negative outcome (0% vs. expected 50%)

✅ "The supplier just informed us the batteries we ordered are discontinued."
- **Why:** Unexpected failure in a planned procurement action

### Type 2: New Risk or Threat
✅ "I just received news that our main competitor launched a similar product at 50% of our price."
- **Why:** New, immediate competitive threat being verbalized for the first time

✅ "The regulatory body just announced new compliance requirements that take effect next month."
- **Why:** New external risk requiring immediate attention

### Type 3: Loss of Shared Understanding
✅ "Wait, I thought we agreed the budget was R$100k, not R$10k. Which is it?"
- **Why:** Explicit realization of misalignment on a critical parameter

✅ "Hold on, are we targeting B2B or B2C? I've been working on B2B materials but you're talking about consumers."
- **Why:** Clear breakdown in shared understanding of strategy

### Type 4: Constraint or Blockage
✅ "We can't launch next week because the legal team hasn't approved the contract yet."
- **Why:** Concrete blockage preventing a planned action

✅ "The cloud provider has a hard limit of 500 concurrent users, so we can't scale as planned."
- **Why:** Technical constraint blocking execution

### Type 5: Forced Reprioritization
✅ "Given the budget cut, we have to abandon the mobile app and focus only on web."
- **Why:** Forced abandonment of a planned feature due to external constraint

✅ "The investor wants to see traction by March, so we're dropping all other features to focus on user acquisition."
- **Why:** External pressure forcing drastic priority change

---

## What IS NOT a Perturbation: Counter-Examples

These are the most common false positives. Study them carefully.

### ❌ Normal Progress and Updates
❌ "We completed the user interviews last week and gathered valuable insights."
- **Why:** Expected progress, no disruption

❌ "The marketing campaign is performing well, we got 200 sign-ups."
- **Why:** Positive expected outcome

### ❌ Routine Planning and Coordination
❌ "Let's schedule the next meeting for Tuesday at 3pm."
- **Why:** Normal coordination, not a forced reorganization

❌ "Can we change the agenda order? Let's discuss the budget first."
- **Why:** Flexible adjustment, not a disruption

### ❌ Proactive Risk Discussion (Future Hypotheticals)
❌ "We should keep an eye on competitor X in case they launch something similar."
- **Why:** Proactive planning about a potential future risk, not a current threat

❌ "If we don't get funding by Q3, we might need to pivot."
- **Why:** Hypothetical scenario, not a current disruption

### ❌ Healthy Debate and Disagreement
❌ "I think we should focus on B2B." / "I disagree, B2C has more potential."
- **Why:** Normal debate. They understand each other, they just disagree on strategy. Only becomes Type 3 if they realize they have different understandings of what was already decided.

❌ "Should we use React or Vue for the frontend?"
- **Why:** Technical discussion, not a breakdown in shared understanding

### ❌ Slow Progress (Without Explicit Blockage)
❌ "The development is taking longer than we hoped, but we're making progress."
- **Why:** Slower pace, but not blocked

❌ "We're still waiting for the designer to finish the mockups."
- **Why:** Normal dependency, not a blockage (unless they explicitly say it's preventing other work)

### ❌ Topic Shifts
❌ "Okay, now let's talk about the marketing plan."
- **Why:** Routine transition between agenda items

### ❌ Coordination Intensification
❌ "Let's have daily check-ins this week to stay aligned."
- **Why:** Amplification of existing coordination patterns, not reorganization

---

## Decision Process for Each Event

For every event in the transcript, ask yourself:

1. **Is this normal, expected discussion or progress?**
   - If YES → **NOT a perturbation**
   - If NO → Continue to step 2

2. **Does it involve a disruption that FORCES the team to stop and reassess/reconsider/reorganize?**
   - If NO → **NOT a perturbation**
   - If YES → Continue to step 3

3. **Can I quote specific dialogue that clearly demonstrates this disruption?**
   - If NO → **NOT a perturbation** (might be implicit, but we only code explicit)
   - If YES → Continue to step 4

4. **Does it fit one of the five types?**
   - Type 1: Unexpected outcome/failure?
   - Type 2: NEW immediate risk/threat (not hypothetical)?
   - Type 3: Explicit loss of shared understanding?
   - Type 4: Concrete blockage preventing action?
   - Type 5: Forced abandonment/reprioritization?
   
   - If YES to any → **PERTURBATION** (classify and justify)
   - If NO to all → **NOT a perturbation**

---

## Analysis Process

### Step 1: Segment the Transcript into Episodes
- Divide the meeting into coherent **episodes** (e.g., "Budget Discussion", "Partnership Review", "Technical Planning")
- Episodes should represent distinct topics or phases of the meeting

### Step 2: Identify Events Within Episodes
- Within each episode, identify **events** — specific moments where something happens:
  - A decision is made
  - Information is revealed
  - A problem is discovered
  - A plan is changed

### Step 3: Flag Perturbations
- For each event, apply the decision process above
- **Be conservative:** When in doubt, do NOT flag as a perturbation
- **Be thorough:** If a genuine perturbation occurred, flag it even if there are already many

### Step 4: Justify Each Perturbation
For every perturbation you flag:
1. **Quote the dialogue** that triggered the classification
2. **State the type** (1-5)
3. **Explain why** it's a perturbation (which criterion it meets)

---

## Output Format

### Table 1: Event Classification
```csv
episode_id,episode_name,event_id,event_name,level,perturbation_flag,perturbation_type,episode_description,event_description
1,Budget Review,1.1,Budget presentation,event,no,,,Budget for Q1 presented
1,Budget Review,1.2,Budget cut announcement,event,yes,4,,CFO announces 30% budget cut preventing planned hires
```

**Critical:** 
- `perturbation_flag` = "yes" or "no" (lowercase)
- `perturbation_type` = 1, 2, 3, 4, or 5 (only if flag = "yes")
- `event_description` = Brief description with justification for perturbations

### Narrative Report Structure
1. **Summary**: 
   - Total perturbations identified
   - Distribution across the five types
   - Brief interpretation (e.g., "This meeting had many Type 4 perturbations, suggesting resource constraints were a major challenge")

2. **Episode-by-Episode Analysis**: 
   - For each episode, list identified perturbations with:
     - Event ID
     - Perturbation type
     - Triggering dialogue (direct quote)
     - Justification (why it meets the criterion)

3. **Conclusion**: 
   - Overall patterns
   - Any notable observations

---

## Quality Control: Self-Check Before Submitting

Before finalizing your analysis, verify:

- [ ] Each perturbation has a **clear textual justification** (direct quote)
- [ ] Each perturbation **fits one of the five types** unambiguously
- [ ] No "normal progress" events are flagged (e.g., "we finished task X")
- [ ] No "routine coordination" events are flagged (e.g., "let's meet next week")
- [ ] No "proactive planning" events are flagged (e.g., "we should watch out for X")
- [ ] No "healthy debates" are flagged unless there's explicit confusion (Type 3)
- [ ] Text summary matches CSV counts exactly
- [ ] All 5 perturbation types are defined in the report
- [ ] Distribution table is included

**Note on quantity:** There is no "correct" number of perturbations. If the meeting was smooth, you may find 5-10. If the meeting was a crisis, you may find 50+. What matters is that each one is justified.

---

## Common Mistakes to Avoid

1. **Flagging routine updates:** "We finished task X" is NOT a perturbation unless it failed
2. **Confusing debate with confusion:** Disagreement ≠ misunderstanding (only Type 3 if they realize they had different understandings)
3. **Flagging future hypotheticals:** "If X happens" is NOT a perturbation unless X just happened
4. **Flagging slow progress as blockage:** Slow ≠ blocked (must be explicitly prevented)
5. **Flagging every decision:** Decisions are normal; only forced changes are perturbations
6. **Over-flagging to be "safe":** It's better to miss a subtle perturbation than to flag normal discussion

---

## Final Reminder

**You are looking for DISRUPTIONS, not discussions.**

Most of a meeting is normal progress. Perturbations are moments when that progress **breaks down** and the team must **stop and reorganize**.

If you find yourself flagging more than ~30-40% of events, you are likely over-flagging. Review your classifications and remove anything that is just normal discussion.

However, if the meeting genuinely had many crises or major changes, it's acceptable to have a high count. The key is that **each one must be justified with clear textual evidence.**
