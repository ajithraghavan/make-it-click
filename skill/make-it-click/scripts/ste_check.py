#!/usr/bin/env python3
"""Rough checker for STE-style writing (in the style of ASD-STE100).

This is a heuristic helper, not a compliance tool. It flags:
  - sentences over the word limit (20 procedural / 25 descriptive)
  - paragraphs with more than 6 sentences
  - -ing words (allowed only inside technical names)
  - likely passive voice
  - perfect tenses
  - common unapproved words, with a suggested replacement

Usage:
  python ste_check.py FILE [--limit 20|25]
  cat text.txt | python ste_check.py -
"""
import re
import sys

SUBSTITUTIONS = {
    "in order to": "to", "utilize": "use", "utilise": "use", "commence": "start",
    "initiate": "start", "terminate": "stop", "ensure": "make sure",
    "prior to": "before", "approximately": "about", "subsequently": "then / after",
    "facilitate": "help", "numerous": "many", "sufficient": "enough",
    "additional": "more", "obtain": "get", "require": "need", "replenish": "fill",
}
ING_ALLOW = {"thing", "things", "string", "strings", "during", "nothing", "something",
             "anything", "everything", "bring", "spring", "ring", "king", "wing", "sing"}
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(\w+ed|\w+en)\b", re.I)
PERFECT = re.compile(r"\b(has|have|had)\s+(\w+ed|\w+en|been)\b", re.I)
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def words(s):
    return re.findall(r"[A-Za-z0-9'-]+", s)


def is_procedural(s):
    w = words(s)
    return bool(w) and w[0].lower() in {
        "make", "close", "open", "remove", "install", "set", "do", "put", "turn",
        "start", "stop", "use", "check", "read", "write", "run", "add", "click", "go"}


def check(text, limit=None):
    issues = []
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for pi, para in enumerate(paragraphs, 1):
        # treat list items as separate sentences
        para_flat = re.sub(r"\n\s*[-*\d.]+\s+", ". ", para).replace("\n", " ")
        sentences = [s for s in SENT_SPLIT.split(para_flat) if words(s)]
        if len(sentences) > 6:
            issues.append((pi, None, f"paragraph has {len(sentences)} sentences (max 6)"))
        for si, s in enumerate(sentences, 1):
            n = len(words(s))
            lim = limit or (20 if is_procedural(s) else 25)
            if n > lim:
                issues.append((pi, si, f"{n} words (limit {lim}): {s[:70]}..."))
            low = s.lower()
            for bad, good in SUBSTITUTIONS.items():
                stem = bad if " " in bad else bad.rstrip("e")
                if re.search(r"\b" + re.escape(stem) + r"\w*\b", low):
                    issues.append((pi, si, f'"{bad}" -> use "{good}"'))
            for w in words(s):
                if w.lower().endswith("ing") and len(w) > 4 and w.lower() not in ING_ALLOW:
                    issues.append((pi, si, f'-ing form "{w}" (OK only in a technical name)'))
            for m in PASSIVE.finditer(s):
                issues.append((pi, si, f'possible passive "{m.group(0)}"'))
            for m in PERFECT.finditer(s):
                issues.append((pi, si, f'perfect tense "{m.group(0)}"'))
    return issues


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    src = sys.argv[1]
    text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    issues = check(text, limit)
    if not issues:
        print("No issues found. (Heuristic check only.)")
        return
    for pi, si, msg in issues:
        loc = f"P{pi}" + (f".S{si}" if si else "")
        print(f"{loc:8} {msg}")
    print(f"\n{len(issues)} possible issue(s). Review each one; some may be false positives.")


if __name__ == "__main__":
    main()
