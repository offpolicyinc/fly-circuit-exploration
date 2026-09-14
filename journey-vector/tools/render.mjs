// Frame-accurate render of the Journey → Vector scene: seek each frame deterministically, screenshot, then encode.
import { chromium } from 'playwright-core';
import { mkdirSync, writeFileSync } from 'node:fs';
// usage: node tools/render.mjs <outDir> [fps] [maxFrames]   (serve the page first: node serve.mjs)
const [,, outDir, fpsArg, limitArg] = process.argv; const FPS = Number(fpsArg) || 30; const LIMIT = Number(limitArg) || Infinity;
mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch({ headless: false, args: ['--use-angle=metal', '--ignore-gpu-blocklist', '--enable-gpu-rasterization', '--window-position=3000,3000'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
await page.goto('http://127.0.0.1:8791/?video', { waitUntil: 'networkidle' });
await page.waitForFunction(() => typeof window.seek === 'function' && document.fonts.status === 'loaded');
await page.evaluate(() => { seek(0); });
await page.waitForTimeout(1500);
const total = await page.evaluate(() => Number(document.getElementById('timeline').max) + 2.4);
const n = Math.min(LIMIT, Math.ceil(total * FPS)); const t0 = Date.now();
for (let i = 0; i < n; i++) {
  const t = i / FPS;
  await page.evaluate(async t => { seek(t); await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); }, t);
  const buf = await page.screenshot({ type: 'png', animations: 'disabled' });
  writeFileSync(`${outDir}/f${String(i).padStart(5, '0')}.png`, buf);
  if (i % 30 === 0) console.log(`frame ${i}/${n} t=${t.toFixed(2)} ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}
await browser.close(); console.log('done', n, 'frames');
