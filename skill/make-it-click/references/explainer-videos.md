# Step 4: Narrated explainer videos

A short, custom video can build intuition that text cannot: a shape that transforms,
an algorithm that runs, a proof that grows one step at a time. The style of the
3Blue1Brown channel (dark background, clean math animation, calm narration) is a good model.

This step needs a code environment. Confirm with the user before you start, because it
takes time and may need an API key.

## Pipeline

1. **Script.** Write the narration first, in STE style (`ste-writing.md`). Short sentences
   are easier to hear. Split the script into scenes; each scene teaches one idea.
   Aim for 1-3 minutes unless the user asks for more.
2. **Storyboard.** For each scene, write one line: what is on screen, what moves, and
   which narration sentence goes with it.
3. **Animation.** Use Manim Community Edition (`pip install manim`) for math and diagram
   animation. One Scene class per scene. Render at low quality first (`-ql`) to check
   timing, then at final quality.
4. **Narration audio.** One audio file per scene.
   - If the user gives an ElevenLabs API key: call the text-to-speech endpoint. Read the
     key from an environment variable (for example `ELEVENLABS_API_KEY`). Never write
     the key into a file, a log, or the output.
   - If there is no key: use a local, free text-to-speech engine (for example Piper or
     Kokoro), or the system voice. Ask the user which they prefer, or pick one that installs.
   - If no audio is possible: make captions only and say so.
5. **Sync.** Measure the length of each audio file. Set the length of each scene to match
   (for example with `self.wait()` in Manim). It is easier to fit animation to audio than
   audio to animation.
6. **Assemble.** Join the scenes and the audio with ffmpeg. Add captions (an `.srt` file)
   made from the script, so the video also works without sound.
7. **Deliver.** One `.mp4` file plus the `.srt` file. Also give the script, so the user can
   edit the text and render again.

## Rules

- One idea per scene. Show it before or while you say it, not after.
- Keep the screen simple: few elements, large labels, consistent colors with one meaning each.
- Put the main point in the first 15 seconds, then build it up.
- End with a short recap scene: 2-4 points.
- If a render fails, fix and render only that scene.
