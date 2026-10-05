# Step 2: Diagrams

A diagram shows shape that prose hides: what connects to what, what comes first, what
is bigger. Use one when the reader must hold several parts in mind at the same time.

## Pick the diagram type from the shape of the content

| Content shape | Diagram |
|---|---|
| Steps in order, with decisions | Flowchart |
| Parts of a system and their links | Block / architecture diagram |
| Messages between actors over time | Sequence diagram |
| States and the events that change them | State diagram |
| Events on a time line | Timeline |
| Parts of a whole, or a hierarchy | Tree |
| Several items compared on the same criteria | Table or annotated grid |
| A change ("before" and "after") | Two panels, side by side |
| Many related facts on one topic | One-page reference sheet with labeled panels |

## Tools, in order of preference

1. A native diagram or visual tool in the current environment, if one exists.
2. Mermaid, for flowcharts, sequences, states, and timelines. It is text, easy to edit,
   and many tools render it.
3. Hand-written SVG, for reference sheets, annotated examples, and anything Mermaid
   cannot lay out well.
4. Graphviz (DOT), for large graphs with automatic layout.

## Rules

- One diagram, one question. If you need two questions, make two diagrams.
- Label every box and arrow. Labels follow the STE rules: short, active, one term per thing.
- Use at most 3 or 4 colors, and give each color one meaning. Do not use color as the only
  carrier of meaning; also use shape, position, or a label.
- Put the most important element at top left or at the center.
- Keep text in boxes short (about 1-6 words). Put detail in a caption or a side note.
- Add a short title that says what the diagram shows.
- After the diagram, write one or two sentences that give the key takeaway.

## Reference sheets

For a dense topic, a "one-page sheet" works well: a grid of lettered panels (A, B, C ...),
each with a title and one kind of content (a structure tree, annotated examples, a table,
a timeline, limits as bars). Annotate examples with callouts that point at the exact words
or parts they explain.
