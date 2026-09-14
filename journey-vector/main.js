// JOURNEY → VECTOR — a hypothesis visualization.
// One arena, one fly, one continuous camera move. Every visual is a pure function of t (seconds), so scrubbing is exact.
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';
import { initBrain } from './brain.js';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';

const PRE = 1.2, FLIGHT = 3.5, MAIN = 20 + (FLIGHT - 3), DUR = PRE + MAIN, HOLD = 2.4;
// beat time: the storyboard is written on a 20 s clock whose first 3 s is the flight; scene time stretches that flight to FLIGHT s
const warp = x => x < 0 ? x : x < FLIGHT ? x * (3 / FLIGHT) : x - (FLIGHT - 3);
const unwarp = b => b < 3 ? b * (FLIGHT / 3) : b + (FLIGHT - 3);
const GOLD = new THREE.Color(1.0, 0.78, 0.34), CORAL = new THREE.Color(1.0, 0.43, 0.38),
      BLUE = new THREE.Color(0.36, 0.78, 1.0), VIOLET = new THREE.Color(0.7, 0.55, 1.0),
      TEAL = new THREE.Color(0.37, 0.9, 0.78), PINK = new THREE.Color(1.0, 0.54, 0.83);
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const clamp01 = x => Math.max(0, Math.min(1, x));
const ss = (a, b, x) => { const k = clamp01((x - a) / (b - a)); return k * k * (3 - 2 * k); };
const ease = x => 1 - Math.pow(1 - clamp01(x), 3);
const backOut = x => { x = clamp01(x); const c = 1.7; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const lerp = (a, b, k) => a + (b - a) * k;
// outbound speed profile: a slow lift-off that gathers pace, then settles before the freeze
const flightProfile = x => { x = clamp01(x); const s = x * x * (3 - 2 * x); return lerp(s, x, 0.15); };

// ---------- renderer / scene ----------
const canvas = document.getElementById('world');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.1;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x1a2028);
scene.fog = new THREE.FogExp2(0x1a2028, 0.009);
const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 200);

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
const bloom = new UnrealBloomPass(new THREE.Vector2(1, 1), 0.45, 0.5, 0.96);
composer.addPass(bloom);
composer.addPass(new OutputPass());

// the big reveal: every light in the kitchen can be pulled down while the unlit diagram stays bright
const dimmable = [], lights = [];
scene.add(new THREE.HemisphereLight(0x9cb8d4, 0x2a241e, 1.1));
// morning sun through the window: low, warm, casting long shadows across the island
const sun = new THREE.DirectionalLight(0xffe3bd, 2.4); sun.position.set(-26, 34, -58); sun.target.position.set(6, 0, -2); scene.add(sun, sun.target);
sun.castShadow = true; sun.shadow.mapSize.set(2048, 2048); sun.shadow.bias = -0.0006; sun.shadow.normalBias = 0.02;
Object.assign(sun.shadow.camera, { left: -40, right: 40, top: 40, bottom: -40, near: 10, far: 140 });
const key = new THREE.DirectionalLight(0xfff1de, 0.7); key.position.set(10, 30, 8); scene.add(key);
const rim = new THREE.DirectionalLight(0xbfd8ff, 1.2); rim.position.set(-10, 40, -60); scene.add(rim);
scene.traverse(o => { if (o.isLight) { o.userData.base = o.intensity; lights.push(o); } });
const pendant = new THREE.SpotLight(0xffd6a0, 90, 90, 0.6, 0.7, 1.4); pendant.userData.base = 90; lights.push(pendant);
const fill = new THREE.PointLight(0xffd2a8, 160, 80, 1.6); fill.position.set(-4, 22, -30); scene.add(fill); fill.userData.base = 160; lights.push(fill); pendant.position.set(8, 30, -4); pendant.target.position.set(6, 0, -2); scene.add(pendant, pendant.target);
const flyLight = new THREE.PointLight(0xffc857, 0, 4, 2); scene.add(flyLight);

// ---------- ground grid ----------
const ground = new THREE.Mesh(new THREE.PlaneGeometry(140, 140), new THREE.ShaderMaterial({
  transparent: true, depthWrite: false,
  uniforms: { uFog: { value: scene.fog.color }, uPulse: { value: 0 }, uPulseCenter: { value: new THREE.Vector3() }, uPulseColor: { value: new THREE.Color(1, 0.78, 0.34) }, uDim: { value: 1 } },
  vertexShader: `varying vec3 vW; void main(){ vec4 w = modelMatrix*vec4(position,1.0); vW=w.xyz; gl_Position = projectionMatrix*viewMatrix*w; }`,
  fragmentShader: `varying vec3 vW; uniform vec3 uFog; uniform float uPulse; uniform vec3 uPulseCenter; uniform vec3 uPulseColor; uniform float uDim;
    float grid(vec2 p, float s, float w){ vec2 g = abs(fract(p/s-0.5)-0.5)/fwidth(p/s); float l = min(g.x,g.y); return 1.0-smoothstep(0.0,w,l); }
    void main(){
      float minor = grid(vW.xz, 1.0, 1.2)*0.22, major = grid(vW.xz, 5.0, 1.4)*0.55;
      float d = length(vW.xz - vec2(6.0,-1.5));
      float fade = 1.0 - smoothstep(12.0, 26.0, d);
      vec3 col = vec3(0.62,0.60,0.55);
      float a = max(minor, major) * fade;
      float ring = 1.0 - smoothstep(0.0, 0.5, abs(length(vW.xz-uPulseCenter.xz) - uPulse*6.0));
      a += ring * (1.0-uPulse) * 0.8 * float(uPulse>0.0);
      gl_FragColor = vec4(mix(col * uDim, uPulseColor, ring*(1.0-uPulse)), a);
    }`
}));
ground.rotation.x = -Math.PI / 2; ground.position.y = 0.004; scene.add(ground);
// ---------- kitchen set (caricature scale: 1 unit ≈ 25 mm; the fly is a chunky 14 mm) ----------
const matte = (c, r = 0.85) => new THREE.MeshStandardMaterial({ color: c, roughness: r, metalness: 0.05 });
const noiseCanvas = (w, h, fn) => { const c = document.createElement('canvas'); c.width = w; c.height = h; fn(c.getContext('2d'), w, h); const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 8; return t; };
// dark stone top with faint veins
const stoneTex = noiseCanvas(1024, 1024, (g, w, h) => {
  g.fillStyle = '#23272b'; g.fillRect(0, 0, w, h);
  for (let i = 0; i < 40000; i++) { const v = 28 + Math.random() * 30; g.fillStyle = `rgba(${v},${v + 2},${v + 5},0.5)`; g.fillRect(Math.random() * w, Math.random() * h, 2, 2); }
  g.strokeStyle = 'rgba(150,158,166,0.16)'; g.lineWidth = 1.2;
  for (let v = 0; v < 26; v++) { g.beginPath(); let x = Math.random() * w, y = Math.random() * h; g.moveTo(x, y); for (let k = 0; k < 30; k++) { x += (Math.random() - 0.5) * 90; y += (Math.random() - 0.5) * 60 + 8; g.lineTo(x, y); } g.stroke(); }
});
stoneTex.repeat.set(3, 2);
const tileTex = noiseCanvas(512, 256, (g, w, h) => {
  g.fillStyle = '#0c0f12'; g.fillRect(0, 0, w, h);
  for (let r = 0; r < 4; r++) for (let c = 0; c < 4; c++) { const off = r % 2 ? w / 8 : 0; const x = c * (w / 4) + off - (r % 2 ? w / 8 : 0), y = r * (h / 4); g.fillStyle = `rgb(${22 + Math.random() * 6},${26 + Math.random() * 6},${31 + Math.random() * 6})`; g.fillRect(x + 3 + (r % 2 ? w / 8 : 0), y + 3, w / 4 - 6, h / 4 - 6); }
});
tileTex.repeat.set(14, 10);
{
  const top = new THREE.Mesh(new THREE.BoxGeometry(72, 2.6, 46), new THREE.MeshPhysicalMaterial({ map: stoneTex, color: 0x8e9398, roughness: 0.62, metalness: 0.02, clearcoat: 0.12, clearcoatRoughness: 0.6 })); top.position.set(4, -1.3, -4); top.receiveShadow = true; scene.add(top);
  const cab = new THREE.Mesh(new THREE.BoxGeometry(70, 34, 44), matte(0x1a1510, 0.8)); cab.position.set(4, -20, -4); scene.add(cab);
  const drawerMat = matte(0x221c15, 0.75), handleMat = new THREE.MeshStandardMaterial({ color: 0x9aa0a6, roughness: 0.3, metalness: 0.9 });
  for (const zf of [18.3, -26.3]) for (let i = 0; i < 4; i++) { const d = new THREE.Mesh(new THREE.BoxGeometry(15.5, 12, 0.6), drawerMat); d.position.set(4 - 26 + i * 17.3, -10, zf); scene.add(d);
    const hd = new THREE.Mesh(new THREE.BoxGeometry(5, 0.5, 0.5), handleMat); hd.position.set(4 - 26 + i * 17.3, -6.5, zf + (zf > 0 ? 0.6 : -0.6)); scene.add(hd); }
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(400, 400), matte(0x0a0c0f, 0.95)); floor.rotation.x = -Math.PI / 2; floor.position.y = -37; scene.add(floor);
  // back wall: subway tile, a window with mullions and a moon, upper cabinets, a shelf of jars
  const wall = new THREE.Mesh(new THREE.PlaneGeometry(400, 160), new THREE.MeshStandardMaterial({ map: tileTex, roughness: 0.6 })); wall.position.set(0, 38, -64); scene.add(wall);
  const win = new THREE.Mesh(new THREE.PlaneGeometry(30, 22), new THREE.MeshBasicMaterial({ color: 0xa8c0d4 })); win.userData.base = 0xa8c0d4; dimmable.push(win); win.position.set(-9, 17, -63.6); scene.add(win);
  const winGlow = new THREE.Mesh(new THREE.PlaneGeometry(38, 30), new THREE.MeshBasicMaterial({ color: 0xffe9c8, transparent: true, opacity: 0.08, blending: THREE.AdditiveBlending, depthWrite: false })); winGlow.position.set(-9, 17, -63.5); scene.add(winGlow);
  const sunDisc = new THREE.Mesh(new THREE.CircleGeometry(2.6, 40), new THREE.MeshBasicMaterial({ color: 0xfff4dc })); sunDisc.userData.base = 0xfff4dc; dimmable.push(sunDisc); sunDisc.position.set(-17, 22, -63.55); scene.add(sunDisc);
  // (no volumetric shafts: the sun and its shadows carry the morning light)
  for (const dx of [-15.2, -5, 5, 15.2]) { const m = new THREE.Mesh(new THREE.BoxGeometry(dx === -15.2 || dx === 15.2 ? 1.4 : 0.9, 23, 0.8), matte(0x0a0c0e)); m.position.set(-9 + dx, 17, -63.2); scene.add(m); }
  for (const dy of [-11.2, 0, 11.2]) { const m = new THREE.Mesh(new THREE.BoxGeometry(31.4, dy === 0 ? 0.9 : 1.4, 0.8), matte(0x0a0c0e)); m.position.set(-9, 17 + dy, -63.2); scene.add(m); }
  for (const [x, w] of [[-50, 26], [18, 26], [50, 30]]) { const c = new THREE.Mesh(new THREE.BoxGeometry(w, 26, 12), matte(0x0c0f12)); c.position.set(x, 24, -58); scene.add(c); }
  const counter = new THREE.Mesh(new THREE.BoxGeometry(200, 36, 12), matte(0x0d1013)); counter.position.set(0, -19, -58); scene.add(counter);
  const counterTop = new THREE.Mesh(new THREE.BoxGeometry(200, 1.2, 13), matte(0x1c2024, 0.5)); counterTop.position.set(0, -0.6, -58); scene.add(counterTop);
  const shelf = new THREE.Mesh(new THREE.BoxGeometry(26, 0.8, 8), matte(0x1a1510)); shelf.position.set(50, 6, -60); scene.add(shelf);
  const jarMat = new THREE.MeshPhysicalMaterial({ color: 0x9fb0bd, roughness: 0.15, transmission: 0.6, thickness: 1.5, transparent: true, opacity: 0.8 });
  for (let i = 0; i < 3; i++) { const j = new THREE.Mesh(new THREE.CylinderGeometry(2.4, 2.4, 6 + i, 24), jarMat); j.position.set(41 + i * 8, 9.4 + i * 0.5, -60); scene.add(j); const lid = new THREE.Mesh(new THREE.CylinderGeometry(2.5, 2.5, 0.8, 24), matte(0x2a2e33, 0.4)); lid.position.set(41 + i * 8, 12.8 + i * 1, -60); scene.add(lid); }
  // pendant lamp above the island
  const shade = new THREE.Mesh(new THREE.ConeGeometry(7, 6, 40, 1, true), new THREE.MeshStandardMaterial({ color: 0x1a1d20, roughness: 0.6, side: THREE.DoubleSide })); shade.position.set(8, 33, -4); scene.add(shade);
  const bulb = new THREE.Mesh(new THREE.SphereGeometry(1.1, 16, 12), new THREE.MeshBasicMaterial({ color: 0xffe3b8 })); bulb.userData.base = 0xffe3b8; dimmable.push(bulb); bulb.position.set(8, 31, -4); scene.add(bulb);
  const cord = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 40, 6), matte(0x0a0a0a)); cord.position.set(8, 56, -4); scene.add(cord);
  // props on the island: cutting board + knife, fruit bowl, mug, salt, folded towel, spoon
  const board = new THREE.Mesh(new RoundedBoxGeometry(16, 1.2, 10, 3, 0.4), matte(0x3a2a1c, 0.7)); board.position.set(-18, 0.6, -12); board.rotation.y = 0.25; board.castShadow = true; scene.add(board);
  const blade = new THREE.Mesh(new THREE.BoxGeometry(9, 0.15, 1.6), new THREE.MeshStandardMaterial({ color: 0xb8bec4, roughness: 0.25, metalness: 0.95 })); blade.position.set(-19, 1.3, -9.5); blade.rotation.y = 0.4; scene.add(blade);
  const knifeHandle = new THREE.Mesh(new THREE.BoxGeometry(4.5, 0.9, 1.1), matte(0x120e0a, 0.6)); knifeHandle.position.set(-12.9, 1.55, -12.1); knifeHandle.rotation.y = 0.4; scene.add(knifeHandle);
  const bowl = new THREE.Mesh(new THREE.CylinderGeometry(6, 3.6, 3.4, 48, 1, true), matte(0x2a2f34, 0.5)); bowl.material.side = THREE.DoubleSide; bowl.position.set(38, 1.7, -19); bowl.castShadow = true; scene.add(bowl);
  const bowlBase = new THREE.Mesh(new THREE.CircleGeometry(3.6, 48), matte(0x2a2f34, 0.5)); bowlBase.rotation.x = -Math.PI / 2; bowlBase.position.set(38, 0.05, -19); scene.add(bowlBase);
  for (const [dx, dz, c] of [[-1.6, 0.6, 0x6a1f1c], [1.7, -0.4, 0x7a2a22], [0.2, 1.9, 0x5d6b2a], [0.1, -1.5, 0x6a1f1c]]) { const a = new THREE.Mesh(new THREE.SphereGeometry(1.9, 24, 18), matte(c, 0.5)); a.position.set(38 + dx, 3.4, -19 + dz); scene.add(a); }
  const mug = new THREE.Group(); const mugMat = matte(0x23282c, 0.45);
  const body = new THREE.Mesh(new THREE.CylinderGeometry(3.2, 2.9, 4.8, 40, 1, true), mugMat); body.material.side = THREE.DoubleSide; body.position.y = 2.4; mug.add(body);
  const bottom = new THREE.Mesh(new THREE.CircleGeometry(2.9, 40), mugMat); bottom.rotation.x = -Math.PI / 2; bottom.position.y = 0.05; mug.add(bottom);
  const coffee = new THREE.Mesh(new THREE.CircleGeometry(3.05, 40), matte(0x120c08, 0.15)); coffee.rotation.x = -Math.PI / 2; coffee.position.y = 4.1; mug.add(coffee);
  const handle = new THREE.Mesh(new THREE.TorusGeometry(1.5, 0.38, 10, 30, Math.PI), mugMat); handle.position.set(3.2, 2.6, 0); handle.rotation.z = -Math.PI / 2; mug.add(handle);
  mug.position.set(-24, 0, 9); mug.rotation.y = 0.6; mug.traverse(o => { if (o.isMesh) o.castShadow = true; }); scene.add(mug);
  const salt = new THREE.Mesh(new THREE.CylinderGeometry(1.1, 1.3, 4, 24), new THREE.MeshPhysicalMaterial({ color: 0xd9dde2, roughness: 0.2, transmission: 0.5, thickness: 1, transparent: true, opacity: 0.9 })); salt.position.set(20, 2, 9); salt.castShadow = true; scene.add(salt);
  const saltCap = new THREE.Mesh(new THREE.CylinderGeometry(1.15, 1.1, 0.9, 24), handleMat); saltCap.position.set(20, 4.4, 9); scene.add(saltCap);
  const towel = new THREE.Mesh(new RoundedBoxGeometry(9, 1.2, 6.5, 3, 0.5), matte(0x2b3a45, 0.95)); towel.position.set(-6, 0.6, 14); towel.rotation.y = -0.2; towel.castShadow = true; scene.add(towel);
  const spoon = new THREE.Group(); const sm = new THREE.MeshStandardMaterial({ color: 0x9aa0a6, roughness: 0.25, metalness: 0.9 });
  const sh = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.18, 6.5), sm); sh.position.z = 3; spoon.add(sh);
  const sb = new THREE.Mesh(new THREE.SphereGeometry(1.2, 20, 12), sm); sb.scale.set(1, 0.32, 1.35); sb.position.z = -0.6; spoon.add(sb);
  spoon.position.set(26, 0.2, -22); spoon.rotation.y = -0.9; scene.add(spoon);
}
// soft ground shadow blob under the fly
const shadowTex = (() => { const c = document.createElement('canvas'); c.width = c.height = 128; const g = c.getContext('2d');
  const r = g.createRadialGradient(64, 64, 0, 64, 64, 64); r.addColorStop(0, 'rgba(0,0,0,.75)'); r.addColorStop(1, 'rgba(0,0,0,0)'); g.fillStyle = r; g.fillRect(0, 0, 128, 128);
  return new THREE.CanvasTexture(c); })();
const shadow = new THREE.Mesh(new THREE.PlaneGeometry(1, 1), new THREE.MeshBasicMaterial({ map: shadowTex, transparent: true, depthWrite: false }));
shadow.rotation.x = -Math.PI / 2; shadow.position.y = 0.012; scene.add(shadow);
// glow sprite texture
const glowTex = (() => { const c = document.createElement('canvas'); c.width = c.height = 128; const g = c.getContext('2d');
  const r = g.createRadialGradient(64, 64, 0, 64, 64, 64); r.addColorStop(0, 'rgba(255,255,255,1)'); r.addColorStop(0.25, 'rgba(255,255,255,.5)'); r.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = r; g.fillRect(0, 0, 128, 128);
  return new THREE.CanvasTexture(c); })();
const sprite = (color, size) => { const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex, color, transparent: true, blending: THREE.AdditiveBlending, depthWrite: false })); s.scale.setScalar(size); return s; };

// ---------- the banana (peeled open, ripe, heavily spotted) ----------
const PERCH = V(0.3, 1.16, 0.3);           // the fly stands on the exposed flesh, a little back from the peeled tip
const FOOD = V(0.3, 1.12, 0.3);
const peelTex = (() => { const c = document.createElement('canvas'); c.width = 1024; c.height = 512; const g = c.getContext('2d');
  const base = g.createLinearGradient(0, 0, 1024, 0); base.addColorStop(0, '#d9b93a'); base.addColorStop(0.15, '#f4d84e'); base.addColorStop(0.5, '#fbe25c'); base.addColorStop(0.85, '#f0d44a'); base.addColorStop(1, '#c9a532');
  g.fillStyle = base; g.fillRect(0, 0, 1024, 512);
  // fine grain
  for (let i = 0; i < 14000; i++) { const v = Math.random(); g.fillStyle = `rgba(${v > 0.5 ? 255 : 90},${v > 0.5 ? 240 : 60},${v > 0.5 ? 150 : 20},${0.05 + Math.random() * 0.08})`; g.fillRect(Math.random() * 1024, Math.random() * 512, 2, 2 + Math.random() * 6); }
  // ridges: five long darker bands
  for (let k = 0; k < 5; k++) { g.fillStyle = 'rgba(120,90,20,0.14)'; g.fillRect(0, k * 102 + 30, 1024, 14); }
  // heavy brown spotting, denser toward both ends
  const spot = (x, y, r, a) => { const rg = g.createRadialGradient(x, y, 0, x, y, r); rg.addColorStop(0, `rgba(58,32,12,${a})`); rg.addColorStop(0.7, `rgba(74,42,16,${a * 0.85})`); rg.addColorStop(1, 'rgba(74,42,16,0)'); g.fillStyle = rg; g.beginPath(); g.ellipse(x, y, r, r * (0.6 + Math.random() * 0.6), Math.random() * 3, 0, Math.PI * 2); g.fill(); };
  for (let i = 0; i < 800; i++) { const x = Math.random() * 1024; const endBias = Math.pow(Math.abs(x / 1024 - 0.5) * 2, 1.5); if (Math.random() > 0.3 + endBias * 0.7) continue; spot(x, Math.random() * 512, 3 + Math.random() * 12, 0.5 + Math.random() * 0.4); }
  for (let i = 0; i < 18; i++) { const x = Math.random() * 1024; spot(x, Math.random() * 512, 16 + Math.random() * 22, 0.3 + Math.random() * 0.3); }
  // bruised tips
  const tip = (x0, w) => { const lg = g.createLinearGradient(x0, 0, x0 + w, 0); lg.addColorStop(0, 'rgba(50,28,10,0.85)'); lg.addColorStop(1, 'rgba(50,28,10,0)'); g.fillStyle = lg; g.fillRect(Math.min(x0, x0 + w), 0, Math.abs(w), 512); };
  tip(0, 70); tip(1024, -90);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 8; return t; })();
const peelMat = new THREE.MeshStandardMaterial({ map: peelTex, color: 0xf2f2f2, roughness: 0.95, metalness: 0.0 });
const peelStripMat = new THREE.MeshStandardMaterial({ map: peelTex, color: 0xf2f2f2, roughness: 0.95, side: THREE.DoubleSide });
const fleshMat = new THREE.MeshStandardMaterial({ color: 0xd8cc9c, roughness: 0.97 });
const stemMat = new THREE.MeshStandardMaterial({ color: 0x3a2a14, roughness: 0.9 });
// swept tube with a radius profile and a 5-ridge cross-section; u0..u1 selects the portion of the spine to sweep
function sweep(curve, radiusAt, u0 = 0, u1 = 1, segs = 120, sides = 28, ridges = true) {
  const geo = new THREE.BufferGeometry(); const P = [], N = [], UVs = [], I = [];
  const fr = curve.computeFrenetFrames(segs, false);
  for (let i = 0; i <= segs; i++) { const u = u0 + (u1 - u0) * i / segs; const p = curve.getPointAt(u); const f = Math.round(u * segs); const nrm = fr.normals[Math.min(f, segs)], bin = fr.binormals[Math.min(f, segs)];
    for (let j = 0; j <= sides; j++) { const th = j / sides * Math.PI * 2; const r = radiusAt(u) * (ridges ? 1 + 0.07 * Math.cos(th * 5) : 1);
      const nx = Math.cos(th) * nrm.x + Math.sin(th) * bin.x, ny = Math.cos(th) * nrm.y + Math.sin(th) * bin.y, nz = Math.cos(th) * nrm.z + Math.sin(th) * bin.z;
      P.push(p.x + nx * r, p.y + ny * r, p.z + nz * r); N.push(nx, ny, nz); UVs.push(u, j / sides); } }
  for (let i = 0; i < segs; i++) for (let j = 0; j < sides; j++) { const a = i * (sides + 1) + j, b = a + sides + 1; I.push(a, b, a + 1, b, b + 1, a + 1); }
  geo.setAttribute('position', new THREE.Float32BufferAttribute(P, 3)); geo.setAttribute('normal', new THREE.Float32BufferAttribute(N, 3)); geo.setAttribute('uv', new THREE.Float32BufferAttribute(UVs, 2)); geo.setIndex(I); return geo;
}
// a peel strip: ribbon along a curve, width tapering toward the free end, outside spotted, inside pale
function ribbon(curve, widthAt, segs = 40) {
  const geo = new THREE.BufferGeometry(); const P = [], UVs = [], I = []; const fr = curve.computeFrenetFrames(segs, false);
  for (let i = 0; i <= segs; i++) { const u = i / segs; const p = curve.getPointAt(u); const b = fr.binormals[i]; const w = widthAt(u);
    for (let k = -1; k <= 1; k += 2) { P.push(p.x + b.x * w * k * 0.5, p.y + b.y * w * k * 0.5, p.z + b.z * w * k * 0.5); UVs.push(0.55 + u * 0.35, k > 0 ? 0.14 : 0.0); } }
  for (let i = 0; i < segs; i++) { const a = i * 2; I.push(a, a + 2, a + 1, a + 1, a + 2, a + 3); }
  geo.setAttribute('position', new THREE.Float32BufferAttribute(P, 3)); geo.setAttribute('uv', new THREE.Float32BufferAttribute(UVs, 2)); geo.setIndex(I); geo.computeVertexNormals(); return geo;
}
const food = new THREE.Group();
function makeBanana(peeled) {
  const g = new THREE.Group();
  // spine lies along local +x, resting on its belly with both tips lifted; the peeled tip is at +x
  const spine = new THREE.CatmullRomCurve3([V(-3.6, 1.0, 0), V(-2.4, 0.7, 0.05), V(-0.8, 0.62, 0), V(1.0, 0.62, -0.05), V(2.6, 0.72, 0), V(3.7, 1.0, 0)], false, 'centripetal');
  const radius = u => 0.6 * Math.pow(Math.sin(Math.PI * Math.min(0.97, Math.max(0.03, u))), 0.32) * (u > 0.92 ? lerp(1, 0.55, (u - 0.92) / 0.08) : 1);
  const split = peeled ? 0.6 : 1.0;
  const peel = new THREE.Mesh(sweep(spine, radius, 0, split), peelMat); peel.castShadow = true; g.add(peel);
  if (peeled) {
    const flesh = new THREE.Mesh(sweep(spine, u => radius(u) * 0.86, 0.54, 0.985, 60, 24, false), fleshMat); flesh.castShadow = true; g.add(flesh);
    const cap = new THREE.Mesh(new THREE.SphereGeometry(radius(0.985) * 0.86, 20, 14), fleshMat); cap.position.copy(spine.getPointAt(0.985)); cap.scale.set(0.5, 1, 1); g.add(cap);
    // four strips peel back from the split, curl outward and droop to the counter
    const sp = spine.getPointAt(split); const tan = spine.getTangentAt(split).normalize();
    for (let k = 0; k < 4; k++) { const th = k / 4 * Math.PI * 2 + 0.5; const side = V(0, Math.cos(th), Math.sin(th)); const r0 = radius(split);
      const up = Math.max(0, Math.cos(th)); // strips near the top curl up and back; lower ones splay out and droop to the counter
      // folded back over the body: each strip stays just outside the peel and droops as it runs toward the stem
      const pts = [sp.clone().addScaledVector(side, r0), sp.clone().addScaledVector(side, r0 * 1.2).addScaledVector(tan, -0.45), sp.clone().addScaledVector(side, r0 * 1.3).addScaledVector(tan, -1.25).add(V(0, -(1 - up) * 0.2, 0)), sp.clone().addScaledVector(side, r0 * 1.35).addScaledVector(tan, -2.0).add(V(0, -(1 - up) * 0.55, 0))];
      for (const p of pts) p.y = Math.max(0.05, p.y);
      const c = new THREE.CatmullRomCurve3(pts, false, 'centripetal'); const geo = ribbon(c, u => r0 * 0.8 * (1 - u * 0.35));
      const strip = new THREE.Mesh(geo, peelStripMat); strip.castShadow = true; g.add(strip); }
  }
  const stem = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.22, 0.9, 10), stemMat); stem.position.copy(spine.getPointAt(0.01)).add(V(-0.35, 0.3, 0)); stem.rotation.z = 1.1; g.add(stem);
  return g;
}
{
  const b1 = makeBanana(true); b1.rotation.y = 0.53; b1.position.set(-1.66, 0, 1.45); food.add(b1);
  const b2 = makeBanana(false); b2.rotation.y = 0.68; b2.position.set(-2.4, 0, -0.2); b2.rotation.z = 0.03; food.add(b2);
  scene.add(food);
}
window.__food = food;

// ---------- flight paths ----------
const outPts = [V(0.3, 1.18, 0.3), V(1.4, 2.0, -0.7), V(3.0, 3.0, -2.5), V(5.4, 3.4, -2.2), V(6.7, 4.6, 0.5), V(8.5, 4.0, 2.0), V(10.4, 5.2, 0.6), V(11.6, 4.6, -1.6)];
const outCurve = new THREE.CatmullRomCurve3(outPts, false, 'centripetal', 0.5);
const P_END = outPts[outPts.length - 1].clone();
const DISP = P_END.clone().sub(FOOD);
const outTan = outCurve.getTangentAt(1).normalize();
const turnEnd = P_END.clone().add(V(-2.2, 0.2, -2.6));
const retPts = [P_END.clone(), P_END.clone().addScaledVector(outTan, 1.3), P_END.clone().add(V(1.5, 0.3, -2.3)), P_END.clone().add(V(-0.3, 0.4, -3.2)), turnEnd,
  turnEnd.clone().lerp(PERCH, 0.3).add(V(0, 0.25, 0)), turnEnd.clone().lerp(PERCH, 0.6).add(V(0, 0.2, 0)), turnEnd.clone().lerp(PERCH, 0.86).add(V(0, 0.25, 0)), PERCH.clone()];
const retCurve = new THREE.CatmullRomCurve3(retPts, false, 'centripetal', 0.5);

// flight-time mapping (fly parameter as function of beat time)
const RET0 = 12.5, RET1 = 17.0, LAND = RET1;
function retParam(t) { if (t < RET0) return 0; if (t >= RET1) return 1; const x = (t - RET0) / (RET1 - RET0); return lerp(x, 1 - Math.pow(1 - x, 2.2), 0.55); } // eases into the landing
function timeScale(t) { return t < 3 ? 1 : t < RET0 ? 0 : t < RET1 ? 1 : 0; }
// accumulated flap phase (closed form) so scrubbing is exact
function flapPhase(t) { const f = 26; let p = f * (FLIGHT / 3) * Math.min(t, 3); if (t > RET0) p += f * (Math.min(t, RET1) - RET0); return p; }
const _p = new THREE.Vector3(), _q = new THREE.Vector3();
function flyPose(t) { // {pos, fwd, yawRate}
  const out = {};
  const pose = (curve, u) => { out.pos = curve.getPointAt(u); out.fwd = curve.getTangentAt(u).normalize(); const u2 = Math.min(1, u + 0.004); const f2 = curve.getTangentAt(u2); out.turn = Math.atan2(out.fwd.x * f2.z - out.fwd.z * f2.x, out.fwd.x * f2.x + out.fwd.z * f2.z) / 0.004; };
  if (t < 3) pose(outCurve, clamp01(flightProfile(t / 3) * 0.999 + 0.0005 * (t / 3)));
  else if (t < 12.5) pose(outCurve, 1);
  else pose(retCurve, retParam(t));
  out.yaw = Math.atan2(out.fwd.x, out.fwd.z);
  return out;
}
const headingOf = fwd => Math.atan2(fwd.x, fwd.z);


// ---------- the synaptic store, as the model computes it ----------
// eight direction columns; while the fly moves, each column's weight grows by the travel-direction bump (rectified cosine)
// times the distance flown. The vector sum of the columns is the stored home vector. Octopamine zeroes every column at food.
const N_COL = 8, STORE_DT = 0.01, STORE_T1 = 21;
const storeTable = (() => { const n = Math.ceil(STORE_T1 / STORE_DT) + 1; const w = new Float32Array(n * N_COL); const acc = new Float32Array(N_COL); let prev = flyPose(0).pos.clone();
  for (let i = 1; i < n; i++) { const t = i * STORE_DT; const P = flyPose(t); const d = P.pos.clone().sub(prev); prev = P.pos.clone(); const ds = Math.hypot(d.x, d.z);
    if (timeScale(t) > 0 && ds > 1e-6) { const h = Math.atan2(d.x, d.z); for (let c = 0; c < N_COL; c++) acc[c] += Math.max(0, Math.cos(h - c * Math.PI * 2 / N_COL)) * ds; }
    const wipe = 1 - ss(LAND + 0.35, LAND + 1.1, t); for (let c = 0; c < N_COL; c++) w[i * N_COL + c] = acc[c] * wipe; }
  return w; })();
const storeWeights = t => { const i = Math.max(0, Math.min(Math.round(t / STORE_DT), storeTable.length / N_COL - 1)); return storeTable.subarray(i * N_COL, i * N_COL + N_COL); };

// ---------- the fly ----------
const fly = new THREE.Group(); scene.add(fly);
const wingL = new THREE.Group(), wingR = new THREE.Group(); const frontLegs = [];
let proboscis;
{
  const bodyMat = new THREE.MeshPhysicalMaterial({ color: 0x4a5a4c, roughness: 0.42, metalness: 0.25, clearcoat: 0.6, clearcoatRoughness: 0.35 });
  const thoraxMat = new THREE.MeshPhysicalMaterial({ color: 0x5a6b58, roughness: 0.38, metalness: 0.3, clearcoat: 0.8, clearcoatRoughness: 0.3 });
  const darkMat = new THREE.MeshStandardMaterial({ color: 0x232a26, roughness: 0.6, metalness: 0.2 });
  const thorax = new THREE.Mesh(new THREE.SphereGeometry(0.135, 32, 24), thoraxMat); thorax.scale.set(1, 0.9, 1.2); thorax.position.z = 0.02; fly.add(thorax);
  for (const x of [-0.05, 0, 0.05]) { const st = new THREE.Mesh(new THREE.BoxGeometry(0.012, 0.005, 0.24), darkMat); st.position.set(x, 0.122, 0.02); fly.add(st); } // thorax stripes
  const scutellum = new THREE.Mesh(new THREE.SphereGeometry(0.07, 20, 14), thoraxMat); scutellum.scale.set(1.1, 0.6, 1); scutellum.position.set(0, 0.06, -0.12); fly.add(scutellum);
  const abdomen = new THREE.Mesh(new THREE.SphereGeometry(0.115, 32, 24), bodyMat); abdomen.scale.set(1, 0.85, 2.2); abdomen.position.set(0, -0.03, -0.29); fly.add(abdomen);
  for (let i = 0; i < 5; i++) { const seg = new THREE.Mesh(new THREE.TorusGeometry(0.108 - i * 0.014, 0.007, 8, 32), darkMat); seg.position.set(0, -0.03, -0.2 - i * 0.075); seg.scale.set(1, 0.85, 1); fly.add(seg); }
  const head = new THREE.Mesh(new THREE.SphereGeometry(0.09, 32, 24), bodyMat); head.scale.set(1.15, 1, 0.9); head.position.set(0, 0.025, 0.21); fly.add(head);
  const eyeMat = new THREE.MeshPhysicalMaterial({ color: 0x6e2a1f, emissive: 0x3a0f0a, emissiveIntensity: 0.6, roughness: 0.22, metalness: 0.1, clearcoat: 1 });
  for (const sgn of [-1, 1]) { const e = new THREE.Mesh(new THREE.SphereGeometry(0.058, 32, 24), eyeMat); e.position.set(sgn * 0.07, 0.04, 0.245); e.scale.set(0.9, 1.25, 1); fly.add(e); }
  proboscis = new THREE.Group(); proboscis.position.set(0, -0.03, 0.26); fly.add(proboscis);
  const pr = new THREE.Mesh(new THREE.CylinderGeometry(0.012, 0.018, 0.16, 8), darkMat); pr.position.y = -0.08; proboscis.add(pr);
  const tip = new THREE.Mesh(new THREE.SphereGeometry(0.03, 12, 8), darkMat); tip.scale.set(1.3, 0.5, 1); tip.position.y = -0.165; proboscis.add(tip);
  for (const sgn of [-1, 1]) { const a = new THREE.Mesh(new THREE.CylinderGeometry(0.005, 0.008, 0.07, 6), darkMat); a.position.set(sgn * 0.025, 0.07, 0.29); a.rotation.x = 0.9; a.rotation.z = sgn * 0.3; fly.add(a); } // antennae
  // legs: three segments, front pair kept for the happy rub
  const legMat = new THREE.MeshStandardMaterial({ color: 0x1c221f, roughness: 0.7 });
  const femur = new THREE.CylinderGeometry(0.011, 0.008, 0.2, 6).translate(0, -0.1, 0), tibia = new THREE.CylinderGeometry(0.008, 0.005, 0.22, 6).translate(0, -0.11, 0), tarsus = new THREE.CylinderGeometry(0.005, 0.003, 0.12, 5).translate(0, -0.06, 0);
  for (const sgn of [-1, 1]) for (let i = 0; i < 3; i++) {
    const hip = new THREE.Group(); hip.position.set(sgn * 0.09, -0.06, 0.1 - i * 0.1); fly.add(hip);
    const f = new THREE.Mesh(femur, legMat); f.rotation.z = sgn * 1.25; f.rotation.x = -0.5 + i * 0.5; hip.add(f);
    const knee = new THREE.Group(); knee.position.set(sgn * 0.19, -0.06, 0); f.add(knee);
    const tb = new THREE.Mesh(tibia, legMat); tb.rotation.z = -sgn * 1.1; knee.add(tb);
    const ankle = new THREE.Group(); ankle.position.set(0, -0.22, 0); tb.add(ankle);
    const ts = new THREE.Mesh(tarsus, legMat); ts.rotation.z = sgn * 0.4; ts.rotation.x = 0.3; ankle.add(ts);
    if (i === 0) frontLegs.push({ hip, sgn, f });
  }
  for (const sgn of [-1, 1]) { const stalk = new THREE.Mesh(new THREE.CylinderGeometry(0.004, 0.004, 0.06, 5), darkMat); stalk.position.set(sgn * 0.13, -0.005, -0.09); stalk.rotation.z = sgn * 1.2; fly.add(stalk); const h = new THREE.Mesh(new THREE.SphereGeometry(0.014, 8, 6), darkMat); h.position.set(sgn * 0.16, 0.0, -0.09); fly.add(h); } // halteres
  // bristles
  const bp = []; for (let i = 0; i < 70; i++) { const th = Math.random() * Math.PI * 2, ph = Math.random() * Math.PI * 0.7; const onAbd = i > 30; const r = onAbd ? 0.11 : 0.13; const cx = 0, cy = onAbd ? -0.03 : 0.0, cz = onAbd ? -0.29 - (Math.random() - .5) * 0.36 : 0.02 + (Math.random() - .5) * 0.2;
    const nx = Math.cos(th) * Math.sin(ph), ny = Math.cos(ph), nz = Math.sin(th) * Math.sin(ph) * 0.3; const L = 0.03 + Math.random() * 0.03;
    bp.push(V(cx + nx * r, cy + ny * r * 0.9, cz), V(cx + nx * (r + L), cy + ny * (r + L) * 0.9, cz - 0.02)); }
  fly.add(new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(bp), new THREE.LineBasicMaterial({ color: 0x2a3230, transparent: true, opacity: 0.7 })));
  // wings
  const shape = new THREE.Shape(); shape.moveTo(0, 0); shape.bezierCurveTo(0.12, 0.085, 0.42, 0.115, 0.6, 0.02); shape.bezierCurveTo(0.5, -0.085, 0.2, -0.1, 0, -0.02);
  const wgeo = new THREE.ShapeGeometry(shape, 24);
  const wmat = new THREE.MeshPhysicalMaterial({ color: 0xd8ecff, transparent: true, opacity: 0.26, roughness: 0.1, metalness: 0.05, iridescence: 1, iridescenceIOR: 1.5, side: THREE.DoubleSide, depthWrite: false });
  const veinMat = new THREE.LineBasicMaterial({ color: 0x9fb8cc, transparent: true, opacity: 0.5 });
  const veins = new THREE.BufferGeometry().setFromPoints([V(0, 0, 0), V(0.58, 0.02, 0), V(0, 0, 0), V(0.5, 0.085, 0), V(0, 0, 0), V(0.44, -0.06, 0), V(0.15, 0.06, 0), V(0.4, 0.09, 0), V(0.2, -0.04, 0), V(0.5, 0.0, 0), V(0.3, 0.07, 0), V(0.34, -0.05, 0)]);
  for (const [g, sgn] of [[wingL, 1], [wingR, -1]]) {
    const m = new THREE.Mesh(wgeo, wmat); m.rotation.x = -Math.PI / 2; m.scale.x = sgn; g.add(m);
    const v = new THREE.LineSegments(veins, veinMat); v.rotation.x = -Math.PI / 2; v.scale.x = sgn; g.add(v);
    g.position.set(sgn * 0.06, 0.09, 0.0); fly.add(g);
  }
  fly.add(flyLight);
  fly.traverse(o => { if (o.isMesh) o.castShadow = true; });
}
const flyGlow = sprite(0xe6eeff, 0.5); scene.add(flyGlow);

// ---------- trails (tube with progress shader) ----------
function makeTrail(curve, color, radius, opacity, additive, dash = 0) {
  const geo = new THREE.TubeGeometry(curve, 320, radius, 8, false);
  const mat = new THREE.ShaderMaterial({
    transparent: true, depthWrite: false, blending: additive ? THREE.AdditiveBlending : THREE.NormalBlending,
    uniforms: { uProgress: { value: 0 }, uOpacity: { value: opacity }, uColor: { value: color }, uHead: { value: 1 }, uDash: { value: dash } },
    vertexShader: `varying vec2 vUv; void main(){ vUv=uv; gl_Position = projectionMatrix*modelViewMatrix*vec4(position,1.0); }`,
    fragmentShader: `varying vec2 vUv; uniform float uProgress,uOpacity,uHead,uDash; uniform vec3 uColor;
      void main(){ if(vUv.x>uProgress) discard; if(uDash>0.5 && fract(vUv.x*uDash)>0.48 && vUv.x<uProgress-0.02) discard; float head = smoothstep(uProgress-0.05,uProgress,vUv.x)*uHead; float tail = smoothstep(0.0,0.03,vUv.x);
      gl_FragColor = vec4(uColor*(1.0+head*0.9), uOpacity*tail*(0.7+0.3*head)); }`
  });
  const m = new THREE.Mesh(geo, mat); m.frustumCulled = false; scene.add(m); return m;
}
const WHITE = new THREE.Color(0.86, 0.9, 0.96);
const trailOut = makeTrail(outCurve, WHITE, 0.013, 0.95, false, 230);
const trailOutGlow = makeTrail(outCurve, WHITE, 0.03, 0.05, true, 0);
const trailRet = makeTrail(retCurve, CORAL, 0.03, 0.95, false);
const trailRetGlow = makeTrail(retCurve, CORAL, 0.08, 0.12, true);

// ---------- arrows ----------
const UP = V(0, 1, 0);
class Arrow {
  constructor(color, r = 0.03, headR = 0.09, headL = 0.22, opacity = 1) {
    this.g = new THREE.Group();
    this.mat = new THREE.MeshBasicMaterial({ color, transparent: true, opacity });
    this.shaft = new THREE.Mesh(new THREE.CylinderGeometry(r, r, 1, 10, 1).translate(0, 0.5, 0), this.mat);
    this.head = new THREE.Mesh(new THREE.ConeGeometry(headR, headL, 16).translate(0, headL / 2, 0), this.mat);
    this.headL = headL; this.g.add(this.shaft, this.head); this.g.visible = false; scene.add(this.g);
  }
  set(a, b, progress = 1, opacity = 1) {
    const d = _p.copy(b).sub(a); const full = d.length(); const L = full * clamp01(progress);
    this.g.visible = L > 0.02 && opacity > 0.005; if (!this.g.visible) return;
    this.g.position.copy(a); this.g.quaternion.setFromUnitVectors(UP, d.normalize());
    const hl = Math.min(this.headL, L * 0.6); this.shaft.scale.y = Math.max(0.001, L - hl); this.head.position.y = L - hl; this.head.scale.setScalar(hl / this.headL);
    this.mat.opacity = opacity;
  }
  hide() { this.g.visible = false; }
}
const N_SEG = 9;
const segPts = Array.from({ length: N_SEG + 1 }, (_, i) => outCurve.getPointAt(i / N_SEG));
const segVec = Array.from({ length: N_SEG }, (_, i) => segPts[i + 1].clone().sub(segPts[i]));
// sorted-by-heading chain: same vectors, reordered → convex arc with the same endpoint (addition is commutative)
const order = Array.from({ length: N_SEG }, (_, i) => i).sort((a, b) => headingOf(segVec[b]) - headingOf(segVec[a]));
const chainStart = []; { let acc = FOOD.clone(); for (const i of order) { chainStart[i] = acc.clone(); acc = acc.clone().add(segVec[i]); } }
const straightStart = [], straightEnd = []; { let acc = 0; const total = segVec.reduce((s, v) => s + v.length(), 0);
  for (const i of order) { straightStart[i] = FOOD.clone().addScaledVector(DISP, acc / total); acc += segVec[i].length(); straightEnd[i] = FOOD.clone().addScaledVector(DISP, acc / total); } }
const segArrows = Array.from({ length: N_SEG }, () => new Arrow(GOLD, 0.022, 0.075, 0.2));
const chainArrows = Array.from({ length: N_SEG }, () => new Arrow(new THREE.Color(1.0, 0.86, 0.5), 0.028, 0.085, 0.2));
const dispArrow = new Arrow(GOLD, 0.075, 0.24, 0.6);
const dispCopy = new Arrow(CORAL, 0.06, 0.2, 0.55);
const homeArrow = new Arrow(CORAL, 0.06, 0.2, 0.55);

// rotation arc (around the fly) for the 180° flip
class Arc {
  constructor(color, n, opacity = 1, additive = false) {
    const geo = new THREE.BufferGeometry(); geo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(n * 3), 3));
    this.line = new THREE.Line(geo, new THREE.LineBasicMaterial({ color, transparent: true, opacity, blending: additive ? THREE.AdditiveBlending : THREE.NormalBlending, depthWrite: false }));
    this.line.frustumCulled = false; this.line.visible = false; scene.add(this.line);
  }
  set(center, radius, a0, a1, y = 0, k = 1) {
    const pos = this.line.geometry.attributes.position; const n = pos.count; const a1k = a0 + (a1 - a0) * k;
    for (let i = 0; i < n; i++) { const a = a0 + (a1k - a0) * i / (n - 1); pos.setXYZ(i, center.x + Math.sin(a) * radius, center.y + y, center.z + Math.cos(a) * radius); }
    pos.needsUpdate = true; this.line.visible = Math.abs(a1k - a0) > 0.01;
  }
  set visible(v) { this.line.visible = v; } get visible() { return this.line.visible; }
  set opacity(o) { this.line.material.opacity = o; }
}
function setArc(arc, center, radius, a0, a1, y = 0, k = 1) { arc.set(center, radius, a0, a1, y, k); }
const rotArc = new Arc(CORAL, 96, 0.95), rotArcGlow = new Arc(CORAL, 96, 0.3, true);
const rotArcHead = new Arrow(CORAL, 0.0001, 0.12, 0.28);

// ---------- camera choreography (one continuous blended move) ----------
const camKeys = [
  { t: -PRE, f: (t, P) => fixed(4.8, 3.3, 8.8, -1.0, 0.9, 0.6) },     // establishing: the banana on the island, kitchen behind
  { t: -0.3, f: (t, P) => fixed(3.9, 2.5, 6.4, -0.5, 1.0, 0.6) },
  { t: 0.2, f: (t, P) => chase(P, 7.5, 2.6, 3.6, 2.2) },
  { t: 2.4, f: (t, P) => chase(P, 7.0, 2.2, -4.2, 1.8) },
  { t: 3.4, f: (t, P) => orbit(P, 8.0, 2.8, 0.9 + (t - 3) * 0.55) },
  { t: 4.6, f: (t, P) => fixed(5.0, 9.0, 17.0, 6.0, 3.4, -3.0) },
  { t: 6.2, f: (t, P) => fixed(2.0, 7.6, 18.5, 6.0, 3.6, -3.5) },
  { t: 9.0, f: (t, P) => fixed(8.0, 7.2, 17.5, 6.6, 3.5, -3.5) },
  { t: 10.6, f: (t, P) => fixed(26.0, 14.0, 8.0, 8.4, 3.4, -4.0) },
  { t: 12.5, f: (t, P) => fixed(24.0, 9.5, 2.5, 10.8, 3.8, -3.5) },
  { t: 13.7, f: (t, P) => chase(P, 6.6, 2.6, -3.2, 1.0, false, 0.6) },
  { t: 15.3, f: (t, P) => chase(P, 6.0, 2.8, 3.4, 1.2) },
  { t: 16.7, f: (t, P) => fixed(5.6, 3.8, 9.0, -0.6, 1.0, 0.4) },        // the landing, seen from the near side of the island
  { t: 18.4, f: (t, P) => fixed(4.6, 3.0, 7.4, -0.5, 1.0, 0.5) },
  { t: 20.0, f: (t, P) => fixed(4.0, 2.6, 6.4, -0.4, 1.0, 0.5) },
];
function chase(P, back, up, side, look, lookGround = false, lat = 0) {
  const right = _q.copy(P.fwd).cross(UP).normalize();
  const pos = P.pos.clone().addScaledVector(P.fwd, -back).addScaledVector(right, side).addScaledVector(UP, up);
  const target = P.pos.clone().addScaledVector(P.fwd, look).addScaledVector(right, lat); if (lookGround) target.y = P.pos.y * 0.5;
  return { pos, target };
}
function orbit(P, r, h, a) { return { pos: V(P.pos.x + Math.cos(a) * r, P.pos.y + h, P.pos.z + Math.sin(a) * r), target: P.pos.clone().addScaledVector(P.fwd, 0.3) }; }
function fixed(x, y, z, tx, ty, tz) { return { pos: V(x, y, z), target: V(tx, ty, tz) }; }
const camPos = new THREE.Vector3(), camTarget = new THREE.Vector3();
const panelEl = document.getElementById('brainpanel');
function panelFraction() { const r = panelEl.getBoundingClientRect(); return r.width > 0 && getComputedStyle(panelEl).display !== 'none' ? r.width / innerWidth : 0; }
function cameraAt(t, P) {
  let i = 0; while (i < camKeys.length - 2 && t >= camKeys[i + 1].t) i++;
  const a = camKeys[i], b = camKeys[i + 1]; const k = ss(0, 1, (t - a.t) / (b.t - a.t));
  const A = a.f(t, P), B = b.f(t, P);
  camPos.lerpVectors(A.pos, B.pos, k); camTarget.lerpVectors(A.target, B.target, k);
  // recentre into the area left of the connectome panel
  const panelFrac = panelFraction(); if (panelFrac > 0) {
    _tmp.subVectors(camTarget, camPos); const d = _tmp.length(); _tmp.normalize(); const rightV = _q.crossVectors(_tmp, UP).normalize();
    const shift = d * Math.tan(THREE.MathUtils.degToRad(camera.fov / 2)) * camera.aspect * panelFrac;
    camPos.addScaledVector(rightV, shift); camTarget.addScaledVector(rightV, shift);
  }
  // handheld float
  camPos.x += Math.sin(t * 0.9) * 0.05; camPos.y += Math.sin(t * 1.3 + 1) * 0.04; camPos.z += Math.cos(t * 0.7) * 0.05;
}

// ---------- DOM callouts ----------
const calloutsEl = document.getElementById('callouts'), leadersEl = document.getElementById('leaders');
const CALLOUTS = [
  { id: 'hdh', name: 'hΔH', color: '#ffc857', tin: 6.0, tout: 9.2, anchor: () => FOOD.clone().addScaledVector(DISP, 0.16), dx: 16, dy: -70 },
  { id: 'hda', name: 'hΔA', color: '#ffc857', tin: 6.35, tout: 9.2, anchor: () => FOOD.clone().addScaledVector(DISP, 0.38), dx: -40, dy: -110 },
  { id: 'hdi', name: 'hΔI', color: '#ffc857', tin: 6.7, tout: 9.2, anchor: () => FOOD.clone().addScaledVector(DISP, 0.60), dx: -30, dy: -150 },
  { id: 'hdg', name: 'hΔG', color: '#ffc857', tin: 7.05, tout: 9.2, anchor: () => FOOD.clone().addScaledVector(DISP, 0.82), dx: -30, dy: -190 },
  { id: 'store', cls: 'qual', name: 'THE SYNAPTIC STORE', color: '#ffc857', tin: 7.5, tout: 9.2, anchor: () => FOOD.clone().addScaledVector(DISP, 0.5).add(V(0, -0.3, 0)), dx: -60, dy: 70, spin: false },
  { id: 'hdm', cls: 'hero', name: 'hΔM', color: '#ff6f61', tin: 10.5, tout: 14.6, anchor: () => rotArcTip(), dx: 40, dy: -40 },
  { id: 'return', cls: 'qual', name: 'THE RETURN PATH', color: '#ff6f61', tin: 12.0, tout: 14.6, anchor: () => P_END.clone().addScaledVector(DISP, -0.45), dx: -80, dy: 70, spin: false },
  { id: 'cancel', cls: 'qual', name: 'HOME VECTOR SHRINKS AS THE STORE CANCELS', color: '#ff6f61', tin: 14.9, tout: 16.4, anchor: () => currentPose.pos.clone().add(V(0, -0.3, 0)), dx: -270, dy: 80, spin: false },
  { id: 'oa', name: 'OA‑VPM3', color: '#5ee6c8', tin: LAND + 0.35, tout: 99, anchor: () => FOOD.clone().add(V(0, 0.25, 0)), dx: 60, dy: -90 },
  { id: 'reset', cls: 'qual', name: 'OCTOPAMINE · RESET AT FOOD', color: '#5ee6c8', tin: LAND + 0.8, tout: 99, anchor: () => FOOD.clone().add(V(0.4, 0.1, 0.4)), dx: -200, dy: 90, spin: false },
];
for (const c of CALLOUTS) {
  const el = document.createElement('div'); el.className = 'callout ' + (c.cls || ''); el.style.color = c.color;
  el.innerHTML = `<div class="name">${c.name}${c.loop ? `<svg class="loop" viewBox="0 0 100 100"><circle class="fill" cx="50" cy="50" r="34"/><path d="M78 36 A34 34 0 1 0 84 56"/><path d="M84 56 L74 44 M84 56 L94 46"/></svg>` : ''}</div>${c.sub ? `<div class="sub">${c.sub}</div>` : ''}`;
  calloutsEl.appendChild(el); c.el = el;
  const line = document.createElementNS('http://www.w3.org/2000/svg', 'path'); line.setAttribute('fill', 'none'); line.setAttribute('stroke', c.color); line.setAttribute('stroke-width', c.cls ? '1' : '1.5'); line.setAttribute('opacity', '0'); leadersEl.appendChild(line); c.line = line;
  const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle'); dot.setAttribute('r', c.cls ? '2.5' : '4'); dot.setAttribute('fill', c.color); dot.setAttribute('opacity', '0'); leadersEl.appendChild(dot); c.dot = dot;
}
let currentPose = flyPose(0);
const anchorState = { rotTip: V(0, 0, 0) };
const rotArcTip = () => anchorState.rotTip;
const _s = new THREE.Vector3();
function updateCallouts(t, W, H) {
  for (const c of CALLOUTS) {
    const kin = ease((t - c.tin) / 0.42), kout = clamp01((t - c.tout) / 0.3);
    const a = kin * (1 - kout); const vis = a > 0.001 && t >= c.tin;
    c.el.style.opacity = vis ? a : 0; c.line.setAttribute('opacity', vis ? a * 0.8 : 0); c.dot.setAttribute('opacity', vis ? a : 0);
    if (!vis) continue;
    _s.copy(c.anchor()).project(camera); const sx = (_s.x * 0.5 + 0.5) * W, sy = (-_s.y * 0.5 + 0.5) * H;
    const stamp = c.spin === false ? 1 : backOut((t - c.tin) / 0.42); const scale = c.spin === false ? 1 : lerp(1.6, 1, stamp); const rot = c.spin === false ? 0 : lerp(-7, 0, stamp);
    const lx = sx + c.dx * (W / 1400 + 0.4), ly = sy + c.dy * (H / 900 + 0.35);
    c.el.style.transform = `translate(${lx.toFixed(1)}px, ${(ly - c.el.offsetHeight).toFixed(1)}px) rotate(${rot.toFixed(2)}deg) scale(${scale.toFixed(3)})`;
    const ex = c.dx < 0 ? lx + c.el.offsetWidth * 0.5 : lx, ey = ly + 4;
    const mx = (ex + sx) / 2, my = ey; // elbow
    c.line.setAttribute('d', `M${ex.toFixed(1)} ${ey.toFixed(1)} L${mx.toFixed(1)} ${my.toFixed(1)} L${sx.toFixed(1)} ${sy.toFixed(1)}`);
    c.dot.setAttribute('cx', sx.toFixed(1)); c.dot.setAttribute('cy', sy.toFixed(1));
  }
}

// ---------- headline / chapters ----------
const headlineEl = document.getElementById('headline'), chapNo = document.getElementById('chapter-no'), chapName = document.getElementById('chapter-name'), eyebrow = document.querySelector('.eyebrow');
const HEADLINES = [
  { no: '01', accent: '#ffc857', tin: 6.3, tout: 9.4, text: "The fly's home vector is not stored in activity,\nbut in synaptic weights of hΔH, hΔA, hΔI and hΔG." },
  { no: '02', accent: '#ff6f61', tin: 11.2, tout: 15.2, text: 'hΔM reverses the memory vector for homing.' },
  { no: '03', accent: '#5ee6c8', tin: LAND + 0.9, tout: 99, text: 'Home! Dopamine gates learning; Octopamine erases the store.' },
];
const CHAPTERS = [[0, '01', 'THE JOURNEY BECOMES MEMORY', '#ffc857'], [9, '02', 'REVERSE IT TO GET HOME', '#ff6f61'], [LAND - 0.2, '03', 'HOME, AND RESET', '#5ee6c8']];
let curHeadline = -1, curChapter = -1;
function updateText(t) {
  let h = -1; HEADLINES.forEach((x, i) => { if (t >= x.tin && t < x.tout) h = i; });
  if (h !== curHeadline) {
    curHeadline = h; headlineEl.innerHTML = '';
    if (h >= 0) { const num = document.createElement('span'); num.className = 'w num'; num.textContent = HEADLINES[h].no; num.style.color = HEADLINES[h].accent; headlineEl.appendChild(num); HEADLINES[h].text.split('\n').forEach((line, li) => { line.split(' ').forEach((w, wi) => { const s = document.createElement('span'); s.className = 'w'; s.textContent = w + ' '; if (/hΔ/.test(w)) s.style.color = HEADLINES[h].accent; s.style.transitionDelay = `${120 + (li * 5 + wi) * 55}ms`; headlineEl.appendChild(s); }); headlineEl.appendChild(document.createElement('br')); }); requestAnimationFrame(() => requestAnimationFrame(() => headlineEl.querySelectorAll('.w').forEach(w => w.classList.add('in')))); }
  }
  let c = 0; CHAPTERS.forEach((x, i) => { if (t >= x[0]) c = i; });
  if (c !== curChapter) { curChapter = c; chapNo.textContent = CHAPTERS[c][1]; chapName.textContent = CHAPTERS[c][2]; eyebrow.style.color = CHAPTERS[c][3]; document.querySelectorAll('nav button').forEach((b, i) => b.classList.toggle('active', i === c)); }
}

// ---------- per-frame scene update (pure function of t) ----------
const _dir = new THREE.Vector3(), _m = new THREE.Matrix4(), _right = new THREE.Vector3(), _up = new THREE.Vector3(), _tmp = new THREE.Vector3();
function update(tScene) {
  const t = warp(tScene - PRE);
  const P = flyPose(Math.max(0, t)); currentPose = P;
  // perched on the banana at both ends: feeding before take-off, and again after the landing
  const kTake = t < 8 ? ss(0, 0.35, t) : 1 - ss(LAND - 0.25, LAND + 0.15, t);
  if (kTake < 1) {
    P.pos.lerpVectors(PERCH, P.pos, kTake); P.pos.y += (1 - kTake) * (0.012 * Math.sin(tScene * 9) + 0.01);
    const feedFwd = V(0.7, -0.25, 0.7).normalize(); P.fwd.lerpVectors(feedFwd, P.fwd, kTake).normalize(); P.yaw = Math.atan2(P.fwd.x, P.fwd.z);
  }
  // fly orientation: forward = tangent, banked into the turn; tipped into the sugar while feeding
  const turn = P.turn || 0;
  const bank = THREE.MathUtils.clamp(-turn * 0.32, -1.0, 1.0);
  _right.copy(UP).cross(P.fwd).normalize(); _up.copy(P.fwd).cross(_right).normalize();
  _m.makeBasis(_right, _up, P.fwd); fly.quaternion.setFromRotationMatrix(_m);
  fly.rotateZ(bank * kTake); fly.rotateX(lerp(0.32, -0.18, kTake));
  fly.position.copy(P.pos);
  const frozen = timeScale(Math.max(0, t)) === 0 || t < 0;
  const kReset = ss(LAND + 0.35, LAND + 1.1, t); // octopamine reset: the store and the drawn memory dissolve
  const flap = frozen ? 0 : Math.sin(flapPhase(t) * Math.PI * 2);
  const wl = (t < 0 || t >= LAND) ? 0.04 : frozen ? 0.15 : 0.35 + flap * 0.85;
  const fold = 1 - kTake; // wings lie flat along the back while feeding
  wingL.rotation.z = wl; wingR.rotation.z = -wl; wingL.rotation.y = lerp(-0.15 + flap * 0.15, 1.3, fold); wingR.rotation.y = lerp(0.15 - flap * 0.15, -1.3, fold);
  // happy: front legs rub together while feeding; proboscis down on the sugar
  for (const L of frontLegs) { L.hip.rotation.x = fold * (0.9 + 0.35 * Math.sin(tScene * 11 + (L.sgn > 0 ? 0 : Math.PI))); L.hip.rotation.y = fold * L.sgn * -0.5; }
  proboscis.rotation.x = lerp(-0.9, 0.35 + 0.1 * Math.sin(tScene * 5), fold);
  fly.position.y += 0;
  // glow + light + shadow
  const flying = !frozen && t >= 0;
  flyGlow.position.copy(P.pos); flyGlow.material.opacity = flying ? 0.32 : 0.1 + 0.08 * Math.sin(t * 3);
  flyLight.intensity = flying ? 0.9 : 0.3;
  shadow.position.set(P.pos.x, 0.012, P.pos.z); const sh = 0.5 + P.pos.y * 0.35; shadow.scale.set(sh, sh * 0.8, 1); shadow.material.opacity = clamp01(1.2 - P.pos.y * 0.3);
  // trails
  const outProg = t < 3 ? flightProfile(t / 3) : 1; const outDim = lerp(1, 0.32, ss(3.6, 5.0, t)) * (1 - kReset);
  trailOut.material.uniforms.uProgress.value = outProg; trailOut.material.uniforms.uOpacity.value = outDim; trailOut.material.uniforms.uHead.value = t < 3 ? 1 : 0;
  trailOutGlow.material.uniforms.uProgress.value = outProg; trailOutGlow.material.uniforms.uOpacity.value = 0.12 * outDim; trailOutGlow.material.uniforms.uHead.value = t < 3 ? 1 : 0;
  const rp = retParam(t); trailRet.material.uniforms.uProgress.value = rp; trailRetGlow.material.uniforms.uProgress.value = rp; trailRet.material.uniforms.uOpacity.value = 0.95 * (1 - kReset); trailRetGlow.material.uniforms.uOpacity.value = 0.14 * (1 - kReset); trailRet.visible = trailRetGlow.visible = rp > 0 && kReset < 1;
  // freeze pulse on the grid
  const resetT = LAND + 0.35; const pulse = t >= 3 && t < 4.2 ? (t - 3) / 1.2 : (t >= 12.5 && t < 13.7 ? (t - 12.5) / 1.2 : (t >= resetT && t < resetT + 1.4 ? (t - resetT) / 1.4 : 0));
  ground.material.uniforms.uPulse.value = pulse; ground.material.uniforms.uPulseCenter.value.copy(t >= resetT ? FOOD : P.pos); ground.material.uniforms.uPulseColor.value.copy(t >= resetT ? TEAL : GOLD);
  // the reveal: 5.9–9.6 s the kitchen goes dark around the four named neurons and the stored vector
  const kReveal = Math.max(ss(5.9, 6.7, t) * (1 - ss(9.0, 9.8, t)), ss(10.2, 11.0, t) * (1 - ss(13.4, 14.4, t))); const dimL = 1 - 0.9 * kReveal;
  for (const l of lights) l.intensity = l.userData.base * dimL;
  for (const m of dimmable) m.material.color.setHex(m.userData.base).multiplyScalar(1 - 0.85 * kReveal);
  scene.background.setHex(0x1a2028).multiplyScalar(1 - 0.8 * kReveal); scene.fog.color.copy(scene.background);
  ground.material.uniforms.uDim.value = 1 - 0.55 * kReveal;
  bloom.strength = 0.35 * kReveal + 0.6 + 1.2 * Math.max(0, 1 - Math.abs(t - 3) * 5) + 1.1 * Math.max(0, 1 - Math.abs(t - 12.5) * 5) + 0.8 * Math.max(0, 1 - Math.abs(t - 10.5) * 4) + 1.0 * Math.max(0, 1 - Math.abs(t - resetT) * 3);

  // --- 3–4s: movement arrows paint along the trail; fade 6.6–8 ---
  const segFade = 1 - ss(6.6, 8.0, t);
  for (let i = 0; i < N_SEG; i++) {
    const k = ease((t - 3.05 - i * 0.075) / 0.32); const a = segPts[i], b = segPts[i + 1];
    const lift = 0.06 + 0.02; // slightly above trail
    if (k > 0 && segFade > 0) segArrows[i].set(_tmp.copy(a).addScaledVector(UP, lift), b.clone().addScaledVector(UP, lift), k, 0.95 * segFade); else segArrows[i].hide();
  }
  // --- 4–6s: copies lift, reorder head-to-tail (sorted by heading → convex arc), then straighten into one line ---
  const kLift = ss(4.0, 5.2, t), kStraight = ss(5.2, 6.0, t), chainFade = 1 - ss(6.2, 7.6, t);
  for (let i = 0; i < N_SEG; i++) {
    if (t < 4.0 || chainFade <= 0) { chainArrows[i].hide(); continue; }
    const s0 = segPts[i], e0 = segPts[i + 1];
    const s1 = chainStart[i].clone().add(V(0, 0.9 * Math.sin(kLift * Math.PI), 0)), e1 = s1.clone().add(segVec[i]);
    const s2 = straightStart[i], e2 = straightEnd[i];
    const S = s0.clone().lerp(s1, kLift).lerp(s2, kStraight), E = e0.clone().lerp(e1, kLift).lerp(e2, kStraight);
    // slight spiral flourish on the way over
    const spin = Math.sin(kLift * Math.PI) * 0.35; S.y += spin * Math.sin(i * 1.7); E.y += spin * Math.sin(i * 1.7 + 0.6);
    chainArrows[i].set(S, E, 1, chainFade * (0.6 + 0.4 * kLift));
  }
  // --- bold displacement arrow draws at 5.7–6.4, persists until unfreeze then dims ---
  const kDisp = ease((t - 5.7) / 0.7); const dispOp = (t < 12.5 ? 1 : lerp(1, 0.35, ss(12.5, 13.5, t))) * (1 - kReset);
  if (kDisp > 0) dispArrow.set(FOOD, P_END, kDisp, dispOp); else dispArrow.hide();
  // --- 9.5–10.5: copy appears at the fly pointing onward; 10.5–12.5 rotates 180° around the fly to point at food; then it rides home with the fly ---
  const kCopy = ease((t - 9.5) / 0.8), kRot = ss(10.5, 12.5, t); const rotOp = 1;
  if (kCopy > 0 && rotOp > 0) {
    const ang = kRot * Math.PI; const dx = DISP.x, dz = DISP.z; const c = Math.cos(ang), s = Math.sin(ang);
    _dir.set(dx * c + dz * s, lerp(DISP.y, -DISP.y, kRot), dz * c - dx * s);
    const SHORT = 0.42; const kExt = ss(12.0, 12.55, t); const len = lerp(SHORT, 1, kExt);
    const tip = P_END.clone().addScaledVector(_dir, len);
    dispCopy.set(P_END, tip, kCopy * (kRot > 0.985 ? 0 : 1), 0.85 * rotOp);
    if (t < RET0) homeArrow.set(P_END, tip, kRot > 0.985 ? kCopy : 0, rotOp);
    else { const rem = FOOD.clone().sub(P.pos); const L = rem.length(); const op = clamp01((L - 1.4) / 1.6); if (L > 1.5) homeArrow.set(P.pos.clone().addScaledVector(rem.clone().normalize(), 0.45), FOOD, 1, op); else homeArrow.hide(); }
    // arc around the fly
    const h0 = Math.atan2(DISP.x, DISP.z); const r = DISP.length() * SHORT * 0.72;
    setArc(rotArc, P_END, r, h0, h0 + Math.PI, 0, kRot); setArc(rotArcGlow, P_END, r, h0, h0 + Math.PI, 0, kRot);
    rotArc.opacity = 0.95 * rotOp * (1 - kExt * 0.6); rotArcGlow.opacity = 0.22 * rotOp;
    const aTip = h0 + Math.PI * kRot; const tipP = V(P_END.x + Math.sin(aTip) * r, P_END.y, P_END.z + Math.cos(aTip) * r);
    anchorState.rotTip.copy(tipP);
    if (kRot > 0.02 && kRot < 0.995) { const tan = V(Math.cos(aTip), 0, -Math.sin(aTip)); rotArcHead.set(tipP.clone().addScaledVector(tan, -0.3), tipP, 1, rotOp); } else rotArcHead.hide();
    if (kRot < 0.02) anchorState.rotTip.copy(P_END).addScaledVector(_dir, SHORT * 0.7);
  } else { dispCopy.hide(); homeArrow.hide(); rotArc.visible = rotArcGlow.visible = false; rotArcHead.hide(); }
  cameraAt(t, P); camera.position.copy(camPos); camera.lookAt(camTarget);
  // subtle dutch during the flip & the bank
  camera.rotateZ(Math.sin(kRot * Math.PI) * 0.06 - bank * 0.08 * (t > 12.5 && t < LAND ? 1 : 0));
}

const brain = initBrain(document.getElementById('brain'), N_COL);
// ---------- playback ----------
let time = 0, playing = true, last = performance.now();
const timeline = document.getElementById('timeline'), timeEl = document.getElementById('time'), playBtn = document.getElementById('play');
function setTime(t) { time = Math.max(0, Math.min(DUR + HOLD, t)); }
function frame(now) {
  requestAnimationFrame(frame);
  const dt = Math.max(0, Math.min(0.05, (now - last) / 1000)); last = now;
  if (playing) { time += dt; if (time > DUR + HOLD) time = 0; }
  const tS = Math.max(0, Math.min(time, DUR)); const t = warp(tS - PRE);
  const W = canvas.clientWidth, H = canvas.clientHeight;
  if (canvas.width !== Math.floor(W * renderer.getPixelRatio()) || canvas.height !== Math.floor(H * renderer.getPixelRatio())) { renderer.setSize(W, H, false); composer.setSize(W, H); camera.aspect = W / H; camera.updateProjectionMatrix(); }
  update(tS); composer.render();
  brain.update(t, tS, { moving: t >= 0 && timeScale(Math.max(0, t)) > 0, heading: currentPose.yaw, weights: storeWeights(Math.max(0, t)), reset: t >= LAND + 0.35 ? 1 - ss(LAND + 0.35, LAND + 1.6, t) : 0, landed: t >= LAND });
  updateCallouts(t, W, H); updateText(t);
  timeline.value = tS; timeline.style.setProperty('--progress', (tS / DUR * 100) + '%');
  timeEl.innerHTML = `${tS.toFixed(1).padStart(4, '0')} <em>/ ${DUR.toFixed(1)}</em>`;
}
timeline.max = DUR; timeline.addEventListener('input', e => { setTime(parseFloat(e.target.value)); });
timeline.addEventListener('pointerdown', () => { playing = false; playBtn.textContent = '▶'; });
playBtn.addEventListener('click', () => { playing = !playing; playBtn.textContent = playing ? 'Ⅱ' : '▶'; });
document.getElementById('restart').addEventListener('click', () => { setTime(0); playing = true; playBtn.textContent = 'Ⅱ'; });

document.querySelectorAll('nav button').forEach(b => b.addEventListener('click', () => { setTime(unwarp(parseFloat(b.dataset.time)) + PRE); playing = true; playBtn.textContent = 'Ⅱ'; }));
addEventListener('keydown', e => {
  if (e.code === 'Space') { e.preventDefault(); playBtn.click(); }
  if (e.code === 'ArrowRight') setTime(time + (e.shiftKey ? 1 : 0.1));
  if (e.code === 'ArrowLeft') setTime(time - (e.shiftKey ? 1 : 0.1));
  if (e.key === 'r') setTime(0);
});
window.__update = (t) => { update(t); updateCallouts(warp(t - PRE), canvas.clientWidth, canvas.clientHeight); };
window.seek = (t) => { setTime(t); playing = false; playBtn.textContent = '▶'; };
if (new URLSearchParams(location.search).has('video')) document.body.classList.add('video');
addEventListener('error', e => { const el = document.getElementById('error'); el.hidden = false; el.textContent = 'Scene error: ' + (e.error && e.error.stack || e.message); });
requestAnimationFrame(frame);
