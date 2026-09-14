// Connectome activity panel: a schematic fly CNS point cloud (brain + ventral nerve cord) whose neuron groups light up
// in step with the main scene. Positions are schematic; the group names and cell counts come from the male CNS tables.
import * as THREE from 'three';

const REGION = { bg: 0, store: 1, hdm: 2, fb3a: 3, ps196: 4, compass: 5, motor: 6 };
const COLORS = [
  new THREE.Color(0.55, 0.6, 0.62), new THREE.Color(1.0, 0.78, 0.34), new THREE.Color(1.0, 0.43, 0.38),
  new THREE.Color(0.36, 0.78, 1.0), new THREE.Color(0.36, 0.78, 1.0), new THREE.Color(0.7, 0.55, 1.0), new THREE.Color(0.9, 0.93, 1.0),
];
const ss = (a, b, x) => { const k = Math.max(0, Math.min(1, (x - a) / (b - a))); return k * k * (3 - 2 * k); };

// seeded random so the cloud is stable between reloads
let seed = 7; const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
const gauss = () => (rnd() + rnd() + rnd() - 1.5) * 1.2;

export function initBrain(canvas) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: false, alpha: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2)); renderer.setClearColor(0x000000, 0);
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(30, 1, 0.1, 50);
  const rig = new THREE.Group(); scene.add(rig);

  const pos = [], rnds = [], regs = [];
  const push = (x, y, z, r) => { pos.push(x, y, z); rnds.push(rnd()); regs.push(r); };
  // ellipsoid blob; bias>1 concentrates points toward the surface (neuropil looks hollow-ish)
  const blob = (n, cx, cy, cz, rx, ry, rz, r = 0, bias = 0.55) => {
    for (let i = 0; i < n; i++) { const u = rnd() * 2 - 1, th = rnd() * Math.PI * 2, rad = Math.pow(rnd(), bias); const s = Math.sqrt(1 - u * u);
      push(cx + rx * rad * s * Math.cos(th), cy + ry * rad * u, cz + rz * rad * s * Math.sin(th), r); }
  };
  // ---- brain ----
  blob(16000, 0, 0, 0, 1.08, 0.72, 0.62);                       // central brain
  blob(9000, -1.62, 0.02, 0.0, 0.7, 0.86, 0.68); blob(9000, 1.62, 0.02, 0.0, 0.7, 0.86, 0.68); // optic lobes
  blob(4200, 0, -0.66, 0.08, 0.55, 0.36, 0.42);                  // subesophageal zone
  blob(1400, -0.5, -0.36, 0.42, 0.2, 0.2, 0.2); blob(1400, 0.5, -0.36, 0.42, 0.2, 0.2, 0.2); // antennal lobes
  blob(1200, -0.95, 0.35, -0.1, 0.22, 0.2, 0.2); blob(1200, 0.95, 0.35, -0.1, 0.22, 0.2, 0.2); // mushroom body calyces
  // ---- central complex ----
  for (let i = 0; i < 1300; i++) { const a = rnd() * Math.PI * 2, rr = 0.2 + gauss() * 0.045; push(Math.cos(a) * rr, -0.03 + gauss() * 0.04, 0.2 + Math.sin(a) * rr * 0.5, REGION.compass); } // ellipsoid body ring (EPG/PEN)
  for (let i = 0; i < 900; i++) { const x = (rnd() * 2 - 1) * 0.58; push(x, 0.3 - 0.16 * x * x + gauss() * 0.025, -0.28 + gauss() * 0.03, REGION.compass); } // protocerebral bridge (PEN/EPG)
  for (let i = 0; i < 1500; i++) { const y = 0.1 + rnd() * 0.2, w = 0.16 + (y - 0.1) * 1.4; const x = (rnd() * 2 - 1) * w; const layer = (y - 0.1) / 0.2;
    push(x, y, 0.02 + gauss() * 0.04 - layer * 0.06, layer > 0.55 ? REGION.store : layer > 0.3 ? REGION.hdm : REGION.fb3a); } // fan-shaped body: upper layers hΔ store, middle hΔM, lower FB3A
  blob(280, -0.14, -0.22, 0.12, 0.05, 0.05, 0.05); blob(280, 0.14, -0.22, 0.12, 0.05, 0.05, 0.05); // noduli
  blob(350, -0.44, -0.2, -0.3, 0.11, 0.1, 0.1, REGION.ps196); blob(350, 0.44, -0.2, -0.3, 0.11, 0.1, 0.1, REGION.ps196); // posterior slope (PS196_b)
  // ---- cervical connective + ventral nerve cord ----
  for (let i = 0; i < 700; i++) push(gauss() * 0.06, -0.82 - rnd() * 0.55, 0.05 + gauss() * 0.05, 0);
  blob(5200, 0, -1.72, 0, 0.5, 0.34, 0.34);                        // prothoracic
  blob(3800, 0, -2.32, 0, 0.56, 0.42, 0.36);                        // mesothoracic (leg)
  blob(1200, 0, -2.2, 0.12, 0.5, 0.2, 0.22, REGION.motor, 0.8);   // dorsal mesothoracic flight neuropil (wing motor)
  blob(5200, 0, -2.92, 0, 0.5, 0.34, 0.34);                        // metathoracic
  blob(3200, 0, -3.5, 0, 0.26, 0.38, 0.22);                         // abdominal
  const N = regs.length;
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  geo.setAttribute('aRnd', new THREE.Float32BufferAttribute(rnds, 1));
  geo.setAttribute('aReg', new THREE.Float32BufferAttribute(regs, 1));
  const uLit = new Float32Array(7);
  const mat = new THREE.ShaderMaterial({
    transparent: true, depthWrite: false, blending: THREE.AdditiveBlending,
    uniforms: { uTime: { value: 0 }, uLit: { value: uLit }, uCol: { value: COLORS }, uAct: { value: 0.4 }, uPix: { value: renderer.getPixelRatio() } },
    vertexShader: `attribute float aRnd, aReg; uniform float uTime, uAct, uPix; uniform float uLit[7]; uniform vec3 uCol[7];
      varying vec3 vC; varying float vA;
      void main(){ int r = int(aReg + 0.5); float lit = uLit[r];
        float tw = 0.5 + 0.5*sin(uTime*(1.5 + aRnd*4.0) + aRnd*60.0);
        float spark = smoothstep(0.975, 1.0, tw) * uAct;
        vec3 grey = uCol[0] * (0.3 + 0.3*tw*uAct + spark*1.2);
        vec3 col = uCol[r] * (0.55 + 0.35*tw);
        vC = mix(grey, col, lit);
        vA = mix(0.028 + 0.04*tw*uAct + spark*0.3, 0.085 + 0.06*tw, lit);
        vec4 mv = modelViewMatrix * vec4(position, 1.0);
        float sz = (0.55 + 0.3*spark) * (1.0 - lit) + (1.1 + 0.5*tw) * lit;
        gl_PointSize = sz * uPix * (2.6 + 110.0 / (mv.z * mv.z));
        gl_Position = projectionMatrix * mv; }`,
    fragmentShader: `varying vec3 vC; varying float vA;
      void main(){ float d = length(gl_PointCoord - 0.5); float a = smoothstep(0.5, 0.12, d); gl_FragColor = vec4(vC, a * vA); }`,
  });
  const points = new THREE.Points(geo, mat); points.frustumCulled = false; rig.add(points);
  // faint outline hint of the body plan: thin midline
  const midline = new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, 0.75, 0.3), new THREE.Vector3(0, -3.9, 0.3)]), new THREE.LineBasicMaterial({ color: 0x1b2430, transparent: true, opacity: 0.5 })); rig.add(midline);

  const legend = Object.fromEntries([...document.querySelectorAll('.bp-legend li')].map(li => [li.dataset.ch, li]));
  let W = 0, H = 0;
  function update(t, tScene, flying) {
    const w = canvas.clientWidth, h = canvas.clientHeight; if (w === 0 || h === 0) return;
    if (w !== W || h !== H) { W = w; H = h; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); }
    // group activity, computed from main-scene time (pure function → scrubbing exact)
    const store = Math.max(ss(6.0, 6.9, t) * (1 - ss(9.2, 9.9, t)), 0.28 * ss(6.0, 6.9, t)); // the store keeps a dim trace once written
    const hdm = ss(10.5, 11.2, t) * (1 - ss(15.2, 15.9, t));
    const fb3a = ss(15.3, 15.8, t) * (1 - ss(17.8, 18.3, t)), ps = ss(15.95, 16.4, t) * (1 - ss(17.8, 18.3, t));
    const loop = ss(18.55, 18.9, t); const compass = ss(18.0, 18.6, t) * (0.75 + 0.25 * Math.sin(tScene * 9) * loop);
    const motor = flying ? 0.85 + 0.15 * Math.sin(tScene * 40) : 0.0;
    uLit[0] = 0; uLit[1] = store; uLit[2] = hdm; uLit[3] = fb3a; uLit[4] = ps; uLit[5] = compass; uLit[6] = motor;
    mat.uniforms.uAct.value = flying ? 0.55 : 0.3; mat.uniforms.uTime.value = tScene;
    legend.motor.classList.toggle('on', motor > 0.2); legend.store.classList.toggle('on', store > 0.2); legend.hdm.classList.toggle('on', hdm > 0.2);
    legend.move.classList.toggle('on', fb3a > 0.2 || ps > 0.2); legend.compass.classList.toggle('on', compass > 0.2);
    // held steady: a fixed three-quarter view with only a slow drift, so the panel reads as a reference, not a show
    rig.rotation.y = 0.32 + Math.sin(tScene * 0.12) * 0.05; rig.rotation.x = -0.12;
    camera.position.set(0, -1.1, 9.0); camera.lookAt(0, -1.4, 0);
    renderer.render(scene, camera);
  }
  return { update, count: N };
}
