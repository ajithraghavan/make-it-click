# Step 3: Interactive HTML explainers

An HTML page lets the reader control the explanation: open details, change a value,
filter a list, step through a process. Use it when a static diagram is not enough.

## Build rules

- One self-contained `.html` file. Inline the CSS and JavaScript. Load libraries only from
  a reliable CDN, at a pinned version. Embed data and images in the file.
- Works without a server. Opens by double-click.
- Responsive: works on a phone and on a desktop. Use relative units and flexbox or grid.
- Support light and dark mode with CSS variables and `prefers-color-scheme`.
- No tracking, no external network calls, no secrets in the file.

## Page structure

1. **Top**: a title and a one-sentence answer to the main question (the ten-second point).
2. **Core visual**: the main diagram, chart, or simulation.
3. **Controls**: only the controls that change the understanding (a slider for a key
   parameter, a step button, a toggle for "before / after").
4. **Layers**: details that the reader can open (`<details>`, tabs, or hover notes).
5. **Bottom**: what to remember, in 3-5 short points.

## Good interactions

- Step-through: "Next" and "Back" buttons for an algorithm or a procedure.
- Parameter slider: the reader changes one input and sees the output change at once.
- Hover or tap annotations on a diagram or a code sample.
- Before / after toggle for a change that an agent made.
- Filter and sort for a long list of findings.

## Animation

Use animation to show change, not to decorate. Keep transitions short (about 200-400 ms).
Respect `prefers-reduced-motion`.

## Text

All text on the page follows the STE rules in `ste-writing.md`.
