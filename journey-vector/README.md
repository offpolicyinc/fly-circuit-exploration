# Journey → Vector

A 20-second hypothesis film: a fly's outbound flight from a banana is frozen and folded into one stored vector,
the vector is flipped by hΔM to point home, the fly flies it back while the store cancels, and octopamine
(OA‑VPM3) wipes the store at the fruit. The right-hand panel draws the circuit computing the same thing.

Everything on screen is a pure function of time, so the scrubber is exact and every render is deterministic.

## Watch it

```
node serve.mjs
```

Then open http://127.0.0.1:8791 . Space pauses, arrow keys step, drag the bar to scrub. Add `?video` to hide the transport.

## Render the video

The page renders itself frame by frame through headless Chromium, then ffmpeg encodes.

```
cd tools && npm install && cd ..
node serve.mjs &
node tools/render.mjs /tmp/frames 30
tools/encode.sh /tmp/frames journey-vector.mp4 30
```

## Files

- `main.js` — scene, fly, banana, kitchen, flight paths, arrows, camera choreography, callouts, timeline
- `brain.js` — the circuit panel (EPG ring, hΔB bump, eight store columns, dopamine gate, octopamine reset)
- `index.html`, `style.css` — page and typography
- `serve.mjs` — static server; `tools/` — render and encode scripts
