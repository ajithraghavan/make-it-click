# make-it-click

An Agent Skill that makes things click: it turns AI output into the format a human understands fastest inspired from Andrej Karpathy's X Post.

As models do more of the work, people spend more time checking and understanding that work.
This skill treats the *format* of an answer as a choice. It picks the lowest step on a
ladder that does the job, and moves up when the content needs it:

1. **Controlled writing** in the style of ASD-STE100 (Simplified Technical English):
   short sentences, active voice, one meaning per word. Strict, "80%", or light.
2. **Diagrams**: flowcharts, architecture, timelines, one-page reference sheets.
3. **Interactive HTML pages**: self-contained, step-through, sliders, before/after.
4. **Narrated explainer videos**: Manim animation + ElevenLabs or free local TTS.

It also has an **oversight mode** for reviewing agent work:
what changed → why → risk → what the human must check.

## Install

**Claude.ai / Claude Desktop:** download `make-it-click.skill` from Releases and add it
under Settings → Capabilities → Skills (or upload the `skill/make-it-click` folder as a zip).

**Claude Code:** copy `skill/make-it-click` into `~/.claude/skills/` (personal) or
`.claude/skills/` in your project.

## Try it

- "Explain how TCP congestion control works, 80% STE."
- "Diagram what this agent changed in the repo and what I need to check."
- "Make an interactive HTML explainer of gradient descent."
- "Create a 3b1b-style video explainer on Fourier series. Use local TTS."

## STE checker

```bash
python skill/make-it-click/scripts/ste_check.py my_text.md
```

A heuristic linter. It flags long sentences, -ing forms, passive voice, perfect tenses,
and common unapproved words. It is **not** a compliance tool.

## Credits and notices

- The idea of the format ladder comes from public notes by Andrej Karpathy on making LLM
  outputs easier to understand. This project is not affiliated with or endorsed by him.
- ASD-STE100 is a specification maintained by ASD (Aerospace, Security and Defence
  Industries Association of Europe). This repository does not contain the specification
  or its dictionary. The rule summary here is written independently and is not
  authoritative. Get the official specification from https://www.asd-ste100.org.
  "ASD-STE100" is used only to refer to that specification.

## License

MIT. See `LICENSE`.
