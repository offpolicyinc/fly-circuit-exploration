// The circuit panel: only the neurons that matter, drawn as a schematic that computes in step with the flight.
//   EPG ring attractor (heading bump)  →  hΔB travel-direction bump  →  eight store columns (hΔH · hΔA · hΔI · hΔG)
//   FB4M · FB1H dopamine gate the write while the fly moves; OA‑VPM3 octopamine zeroes the store at food.
// Everything drawn is a function of the state handed in each frame, so scrubbing is exact.
const TAU = Math.PI * 2;
const ss = (a, b, x) => { const k = Math.max(0, Math.min(1, (x - a) / (b - a))); return k * k * (3 - 2 * k); };
const C = { ink: '#e8ebe6', dim: '#5f717a', faint: 'rgba(120,140,150,0.22)', gold: '#ffc857', coral: '#ff6f61', violet: '#b48cff', pink: '#ff8ad4', teal: '#5ee6c8', white: '#f4f7ff' };
const rgba = (hex, a) => { const n = parseInt(hex.slice(1), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; };

export function initBrain(canvas, N_COL) {
  const g = canvas.getContext('2d');
    let W = 0, H = 0, dpr = 1;
  const mono = px => `500 ${px}px "IBM Plex Mono", monospace`, cond = px => `700 ${px}px "Barlow Condensed", sans-serif`;
  const label = (text, x, y, color, px = 9, align = 'center', font = mono) => { g.font = font(px); g.fillStyle = color; g.textAlign = align; g.textBaseline = 'middle'; g.fillText(text, x, y); };
  const glowDot = (x, y, r, color, lit) => {
    if (lit > 0.01) { const rg = g.createRadialGradient(x, y, 0, x, y, r * 4); rg.addColorStop(0, rgba(color, 0.55 * lit)); rg.addColorStop(1, rgba(color, 0)); g.fillStyle = rg; g.beginPath(); g.arc(x, y, r * 4, 0, TAU); g.fill(); }
    g.fillStyle = lit > 0.01 ? color : rgba(color, 0.3); g.beginPath(); g.arc(x, y, r, 0, TAU); g.fill();
  };
  const link = (x0, y0, x1, y1, color, lit, dash = [3, 4]) => { g.strokeStyle = rgba(color, 0.18 + 0.7 * lit); g.lineWidth = 1 + lit; g.setLineDash(dash); g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke(); g.setLineDash([]); };
  const arrowHead = (x, y, ang, size, color) => { g.fillStyle = color; g.beginPath(); g.moveTo(x, y); g.lineTo(x - Math.cos(ang - 0.45) * size, y - Math.sin(ang - 0.45) * size); g.lineTo(x - Math.cos(ang + 0.45) * size, y - Math.sin(ang + 0.45) * size); g.closePath(); g.fill(); };
  let peakW = 1; // running scale for the wedges: the largest weight seen so far, so the rose grows into its frame

  function update(t, tScene, S) {
    const w = canvas.clientWidth, h = canvas.clientHeight; if (w === 0 || h === 0) return;
    dpr = Math.min(devicePixelRatio, 2);
    if (w !== W || h !== H) { W = w; H = h; canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr); }
    g.setTransform(dpr, 0, 0, dpr, 0, 0); g.clearRect(0, 0, W, H);
    const moving = S.moving ? 1 : 0, reset = S.reset || 0;
    const weights = S.weights; let wmax = 0, sx = 0, sy = 0;
    for (let c = 0; c < N_COL; c++) { const a = c * TAU / N_COL; wmax = Math.max(wmax, weights[c]); sx += Math.sin(a) * weights[c]; sy += Math.cos(a) * weights[c]; }
    peakW = Math.max(peakW, wmax);
    const storeLit = wmax > 0.05 ? 1 : 0; const sumLen = Math.hypot(sx, sy);
    const cx = W * 0.5; const unit = Math.min(W, H * 0.62);

    // ---- EPG ring attractor: heading bump ----
    const ry = H * 0.16, rr = unit * 0.16;
    g.strokeStyle = rgba(C.violet, 0.25); g.lineWidth = 1.2; g.beginPath(); g.arc(cx, ry, rr, 0, TAU); g.stroke();
    const nRing = 16; const heading = S.heading || 0;
    for (let i = 0; i < nRing; i++) { const a = i * TAU / nRing; let d = a - heading; d = Math.atan2(Math.sin(d), Math.cos(d)); const bump = Math.exp(-(d * d) / 0.32) * (S.landed ? 0.55 : 1);
      // screen angle: heading 0 = up, clockwise positive (matches the rose below)
      const x = cx + Math.sin(a) * rr, y = ry - Math.cos(a) * rr; glowDot(x, y, 2 + bump * 2.6, C.violet, bump); }
    label('EPG', cx, ry + rr + 14, C.violet, 11, 'center', cond);

    // ---- hΔB travel-direction bump: a short strip of eight columns ----
    const by = ry + rr + 36, bw = unit * 0.5, bx0 = cx - bw / 2, cellW = bw / N_COL;
    for (let c = 0; c < N_COL; c++) { const a = c * TAU / N_COL; let d = a - heading; d = Math.atan2(Math.sin(d), Math.cos(d)); const v = Math.max(0, Math.cos(d)) * moving;
      g.fillStyle = rgba(C.white, 0.08 + 0.75 * v); g.fillRect(bx0 + c * cellW + 1, by - 5, cellW - 2, 10); }
    label('hΔB', cx, by + 17, C.dim, 10, 'center', cond);
    link(cx, ry + rr + 2, cx, by - 7, C.violet, moving * 0.6, [2, 3]);

    // ---- the store: eight columns as a rose of wedges; the vector sum is the home vector ----
    const oy = by + 40 + unit * 0.27, R = unit * 0.25;
    link(cx, by + 24, cx, oy - R - 14, C.gold, moving, [2, 3]);
    g.strokeStyle = C.faint; g.lineWidth = 1; g.beginPath(); g.arc(cx, oy, R, 0, TAU); g.stroke();
    g.beginPath(); g.arc(cx, oy, R * 0.5, 0, TAU); g.stroke();
    for (let c = 0; c < N_COL; c++) { const a = c * TAU / N_COL; g.strokeStyle = C.faint; g.beginPath(); g.moveTo(cx, oy); g.lineTo(cx + Math.sin(a) * R, oy - Math.cos(a) * R); g.stroke(); }
    const scale = R / Math.max(peakW, 1e-3);
    for (let c = 0; c < N_COL; c++) { const a = c * TAU / N_COL; const len = Math.min(R, weights[c] * scale); if (len < 0.5) continue;
      const half = TAU / N_COL * 0.42; let d = a - heading; d = Math.atan2(Math.sin(d), Math.cos(d)); const writing = Math.max(0, Math.cos(d)) * moving;
      g.fillStyle = rgba(C.gold, 0.28 + 0.35 * writing); g.strokeStyle = rgba(C.gold, 0.7 + 0.3 * writing); g.lineWidth = 1;
      g.beginPath(); g.moveTo(cx, oy); g.arc(cx, oy, len, a - half - Math.PI / 2, a + half - Math.PI / 2); g.closePath(); g.fill(); g.stroke(); }
    // reset flash: a teal ring collapsing inward over the rose
    if (reset > 0) { g.strokeStyle = rgba(C.teal, reset); g.lineWidth = 2 + 6 * reset; g.beginPath(); g.arc(cx, oy, R * (0.2 + 0.9 * (1 - reset)), 0, TAU); g.stroke(); }
    // home vector = vector sum
    if (sumLen * scale > 2) { const ex = cx + sx * scale * 0.98, ey = oy - sy * scale * 0.98; g.strokeStyle = C.gold; g.lineWidth = 2.5; g.shadowColor = C.gold; g.shadowBlur = 10; g.beginPath(); g.moveTo(cx, oy); g.lineTo(ex, ey); g.stroke(); g.shadowBlur = 0; arrowHead(ex, ey, Math.atan2(ey - oy, ex - cx), 9, C.gold); }
    glowDot(cx, oy, 2.2, C.gold, storeLit);
    label('hΔH · hΔA · hΔI · hΔG', cx, oy + R + 18, storeLit ? C.gold : C.dim, 11, 'center', cond);

    // ---- dopamine write gate on the left, octopamine reset on the right ----
    const gx = 12, gy = oy - R * 0.3; const dop = moving;
    glowDot(gx, gy, 4.5, C.pink, dop); link(gx + 5, gy, cx - R * 0.72, oy - R * 0.2, C.pink, dop);
    label('FB4M · FB1H', gx - 4, gy - 26, dop ? C.pink : C.dim, 10, 'left', cond); label('DOPAMINE', gx - 4, gy - 14, C.dim, 6.5, 'left');
    const ox = W - 12, oyy = oy + R * 0.3; const oa = Math.min(1, reset * 1.6);
    glowDot(ox, oyy, 4.5, C.teal, oa); link(ox - 5, oyy, cx + R * 0.72, oy + R * 0.2, C.teal, oa);
    label('OA‑VPM3', ox + 4, oyy + 16, oa > 0.05 ? C.teal : C.dim, 10, 'right', cond); label('OCTOPAMINE', ox + 4, oyy + 28, C.dim, 6.5, 'right');

  }
  return { update };
}
