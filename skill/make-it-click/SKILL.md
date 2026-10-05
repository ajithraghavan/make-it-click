---
name: make-it-click
description: Turn any explanation, summary, or AI/agent output into the format a human can understand fastest. Picks from a ladder of formats (controlled-language writing in the style of ASD-STE100 Simplified Technical English, diagrams, interactive HTML pages, narrated explainer videos) and produces it. Use this skill whenever the user asks to explain, summarize, simplify, or "help me understand" something; asks for "STE", "ASD-STE100", "Simplified Technical English", "plain/clear/readable" writing, or "80% STE"; asks to "diagram it", "show me", "make it in HTML", "make an explainer", or a "3Blue1Brown / 3b1b style video"; or needs to review, audit, or oversee what an LLM or agent produced (diffs, logs, long reports, research output). Use it even when the user does not name a format but the content is complex enough that plain prose would be hard to read.
---

# Make It Click

Models now do more of the work. People spend more of their time checking and understanding
that work. This skill makes the output easy to understand. It treats the format of an answer
as a choice, not a default, and it moves up a ladder of formats when the content needs it.

Idea credit: Andrej Karpathy's public notes on making LLM outputs easier to understand.

## The ladder

Each step costs more to make and gives more understanding. Pick the lowest step that does
the job, unless the user asks for a specific step.

| Step | Format | Best for | Reference |
|---|---|---|---|
| 1 | Controlled writing (STE style) | Instructions, explanations, summaries, anything read once | `references/ste-writing.md` |
| 2 | Diagram | Structure, flow, relationships, comparisons, timelines | `references/diagrams.md` |
| 3 | Interactive HTML page | Content with several layers, data to explore, parameters to change | `references/html-explainers.md` |
| 4 | Narrated explainer video | Concepts that change over time, math, intuition building, teaching | `references/explainer-videos.md` |

Read only the reference file for the step you use. Read `ste-writing.md` for every step,
because the words in diagrams, pages, and narration follow the same rules.

## How to choose

1. If the user names a format, use that format.
2. If the content has a shape (parts that connect, steps that branch, values that change),
   go to step 2 or higher. Prose hides shape.
3. If the user will want to poke at it (change a value, expand a detail, filter a list),
   go to step 3.
4. If the idea depends on motion or build-up (a transform, an algorithm running, a proof
   step by step), offer step 4. Videos take time and may need API keys, so confirm before
   you build one unless the user asked for it.
5. Otherwise, use step 1.

When in doubt, give a short step-1 answer and offer the next step in one line.

## STE strength levels

Users can ask for different strengths. Default to "80%" when the user does not say.

- **Strict**: follow every rule in `ste-writing.md`, including the approved-word list.
- **80% (default)**: follow the sentence, verb, and structure rules. Allow normal words when
  no simple word exists, and allow a few longer sentences to keep the text natural.
- **Light**: short sentences, active voice, one idea per sentence. No other rules.

## Oversight mode

Use this mode when the user must check work that a model or agent did (code changes, a
research report, a long log, a data pipeline). Make the output answer these questions,
in this order:

1. What changed or what was found? (one sentence)
2. Why? (the reason or the evidence)
3. What is the risk? (what can break, what is not certain)
4. What must the human check? (a short list of specific things to look at)

Put uncertainty in the open. Mark claims that you did not verify. A diagram of "before"
and "after" is often the fastest way to show a change.

## Disposable artifacts

Pages and videos made with this skill are for one person and one question. Do not
over-engineer them. Make them self-contained (one HTML file, one video file), make them
fast, and do not add features the user did not ask for. It is acceptable to discard them
after use.

## Quality check before you deliver

- Can the user get the main point in ten seconds?
- Does each sentence, label, or scene carry one idea?
- Is the same term used for the same thing everywhere?
- For steps 2-4: do the words also pass the step-1 rules?
- Optional: run `python scripts/ste_check.py <file>` on written text to flag long
  sentences, -ing forms, passive voice, and common unapproved words.
