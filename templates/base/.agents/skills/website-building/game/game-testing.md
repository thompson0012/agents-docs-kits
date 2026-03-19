# Game Testing & Development

**Prerequisite:** Read `.agents/skills/website-building/shared/12-playwright-interactive.md` for the current browser automation workflow.

Build games in small steps and validate every change. Treat each iteration as: implement → act → pause → observe → adjust.

## Workflow

1. **Pick a goal.** Define a single feature or behavior to implement.
2. **Implement small.** Make the smallest change that moves the game forward.
3. **Ensure integration points.** Provide a single primary game surface and `window.render_game_to_text` so the browser QA loop can read state.
4. **Add `window.advanceTime(ms)`.** Strongly prefer a deterministic step hook so the browser tool can advance frames reliably when timing matters.
5. **Start or confirm the local runtime.** Use the stack's normal shell command from the project directory.
6. **Open the browser session and navigate to the local URL.** Keep one session open while you iterate.
7. **Use `observe` before interacting.** Map visible controls and stable element IDs before clicks, typing, or keyboard input.
8. **Drive one scenario at a time with real input.** Use normal browser actions for controls. Use `evaluate` only for deterministic hooks such as `window.advanceTime(ms)` or `window.render_game_to_text()`.
9. **Inspect state after each burst.** Compare observed UI, screenshots, and text state before moving on.
10. **Inspect screenshots when visual evidence matters.** Save them, review them with the image-inspection tool, fix issues, and rerun.
11. **Verify controls and state (multi-step focus).** Exhaustively exercise all important interactions. For each, think through the full multi-step sequence it implies (cause → intermediate states → outcome) and verify the entire chain works end-to-end. Confirm `render_game_to_text` reflects the same state shown on screen. If anything is off, fix and rerun.
  Examples of important interactions: move, jump, shoot/attack, interact/use, select/confirm/cancel in menus, pause/resume, restart, and any special abilities or puzzle actions defined by the request. Multi-step examples: shooting an enemy should reduce its health; when health reaches 0 it should disappear and update the score; collecting a key should unlock a door and allow level progression.
12. **Check errors.** Review browser console output and local runtime logs. Fix the first new issue before continuing.
13. **Reset between scenarios.** Avoid cross-test state when validating distinct features.
14. **Iterate with small deltas.** Change one variable at a time (frames, inputs, timing, positions), then repeat steps 8–13 until stable.

Example browser QA loop:

- Start the local runtime with the project's normal dev command.
- Open the browser automation tool, `goto` the local URL, and `observe` the page.
- Use `click_id`, `press`, or other normal actions for gameplay, then `evaluate` `window.advanceTime?.(250)` when deterministic stepping helps.
- Use `evaluate` to read `window.render_game_to_text?.()`, and capture screenshots only when they add evidence.

## Test Checklist

Test any new features added for the request and any areas your logic changes could affect. Identify issues, fix them, and re-run the tests to confirm they’re resolved.

Examples of things to test:

- Primary movement/interaction inputs (e.g., move, jump, shoot, confirm/select).
- Win/lose or success/fail transitions.
- Score/health/resource changes.
- Boundary conditions (collisions, walls, screen edges).
- Menu/pause/start flow if present.
- Any special actions tied to the request (powerups, combos, abilities, puzzles, timers).

## Test Artifacts to Review

- Latest screenshots from the browser QA pass.
- Latest `render_game_to_text` JSON output.
- Console error logs (fix the first new error before continuing).
You must actually review the latest screenshots after capturing them, not just generate them. Ensure everything that should be visible on screen is actually visible. Go beyond the start screen and capture gameplay screenshots that cover all newly added features. Treat the screenshots as the source of truth; if something is missing, it is missing in the build. If a screenshot disagrees with what the browser tool reported, investigate the mismatch before signoff. Fix and rerun in a tight loop until the screenshots and text state look correct. Once fixes are verified, re-test all important interactions and controls, confirm they work, and ensure your changes did not introduce regressions. If they did, fix them and rerun everything in a loop until interactions, text state, and controls all work as expected. Be exhaustive in testing controls; broken games are not acceptable.

## Core Game Guidelines

### Canvas + Layout

- Prefer a single canvas centered in the window.

### Visuals

- Keep on-screen text minimal; show controls on a start/menu screen rather than overlaying them during play.
- Avoid overly dark scenes unless the design calls for it. Make key elements easy to see.
- Draw the background on the canvas itself instead of relying on CSS backgrounds.

### Generated Art Assets

When generating game sprites, tiles, or UI elements, use transparent backgrounds so the exported PNGs are ready for compositing.

### Text State Output (render_game_to_text)

Expose a `window.render_game_to_text` function that returns a concise JSON string representing the current game state. The text should include enough information to play the game without visuals.

Minimal pattern:

```js
function renderGameToText() {
  const payload = {
    mode: state.mode,
    player: { x: state.player.x, y: state.player.y, r: state.player.r },
    entities: state.entities.map((e) => ({ x: e.x, y: e.y, r: e.r })),
    score: state.score,
  };
  return JSON.stringify(payload);
}
window.render_game_to_text = renderGameToText;
```

Keep the payload succinct and biased toward on-screen/interactive elements. Prefer current, visible entities over full history.
Include a clear coordinate system note (origin and axis directions), and encode all player-relevant state: player position/velocity, active obstacles/enemies, collectibles, timers/cooldowns, score, and any mode/state flags needed to make correct decisions. Avoid large histories; only include what's currently relevant and visible.

### Waiting for Game State

Use the browser tool's `evaluate` action to poll `render_game_to_text` for state transitions instead of relying on blind timeouts:

```javascript
() => {
  try {
    return JSON.parse(window.render_game_to_text()).phase === 'racing';
  } catch {
    return false;
  }
}
```

### Time Stepping Hook

Provide a deterministic time-stepping hook so the browser tool can advance the game in controlled increments. Expose `window.advanceTime(ms)` (or a thin wrapper that forwards to your game update loop) and have the game loop use it when present.
Use this hook for reproducible automated checks, then confirm the same behavior with normal browser input before signoff.

Minimal pattern:

```js
window.advanceTime = (ms) => {
  const steps = Math.max(1, Math.round(ms / (1000 / 60)));
  for (let i = 0; i < steps; i++) update(1 / 60);
  render();
};
```

### Viewport Fit and Resize

- Fullscreen API is not available in the sandbox; design the game to fill the iframe viewport instead.
- On resize or orientation change, resize the canvas or render target and keep input mapping aligned with the visible game surface.
- Re-check desktop and narrow mobile widths during browser QA so the initial playable view remains usable.

## Debug Overlay (Required)

Every game must include a performance overlay visible in screenshots. Keep visible by default; only hide when the user explicitly requests a clean build.

### Three.js Debug HUD

```javascript
class DebugOverlay {
  constructor(renderer) {
    this.renderer = renderer;
    this.el = document.createElement('div');
    this.el.style.cssText = `
      position:fixed;top:0;left:0;z-index:99999;
      background:rgba(0,0,0,.75);color:#0f0;
      font:11px/1.5 monospace;padding:6px 10px;
      pointer-events:none;white-space:pre;
    `;
    document.body.appendChild(this.el);
    this.frames = 0;
    this.lastTime = performance.now();
    this.lastFrameTime = performance.now();
    this.frameTimes = [];
  }

  update() {
    const now = performance.now();
    this.frameTimes.push(now - this.lastFrameTime);
    this.lastFrameTime = now;
    this.frames++;

    if (now - this.lastTime >= 1000) {
      const fps = (this.frames * 1000) / (now - this.lastTime);
      const avg = this.frameTimes.reduce((a, b) => a + b, 0) / this.frameTimes.length;
      const max = Math.max(...this.frameTimes);
      const info = this.renderer?.info;

      const lines = [`FPS:${fps.toFixed(0)} Frame:${avg.toFixed(1)}ms (max ${max.toFixed(1)}ms)`];
      if (info) lines.push(`Draw:${info.render?.calls} Tri:${info.render?.triangles} Geo:${info.memory?.geometries} Tex:${info.memory?.textures}`);
      if (performance.memory) lines.push(`Heap:${(performance.memory.usedJSHeapSize/1048576).toFixed(1)}MB`);

      const warn = [];
      if (fps < 30) warn.push('⚠LOW FPS');
      if (info?.render?.calls > 200) warn.push('⚠DRAW CALLS');
      if (info?.memory?.geometries > 500) warn.push('⚠GEO LEAK');
      if (warn.length) lines.push(warn.join(' '));

      this.el.textContent = lines.join('\n');
      this.frames = 0; this.lastTime = now; this.frameTimes = [];
    }
  }
}
// Usage: const debug = new DebugOverlay(renderer); call debug.update() each frame
```

### 2D Canvas FPS Counter

```javascript
let _frames = 0, _last = performance.now(), _fps = 0, _ft = 0, _prev = 0;
function updateDebug() {
  _frames++; const n = performance.now(); _ft = n - (_prev||n); _prev = n;
  if (n - _last >= 1000) { _fps = (_frames*1000)/(n-_last); _frames=0; _last=n; }
}
function drawDebug(ctx) {
  ctx.save(); ctx.fillStyle='rgba(0,0,0,.75)'; ctx.fillRect(0,0,200,20);
  ctx.font='11px monospace'; ctx.fillStyle=_fps<30?'#f44':'#0f0';
  ctx.fillText(`FPS:${_fps.toFixed(0)} ${_ft.toFixed(1)}ms`,6,14); ctx.restore();
}
```

## Runtime Tweaking with lil-gui

Use **lil-gui** (`import GUI from 'https://esm.sh/lil-gui'`) for live parameter adjustment:

```javascript
const params = { gravity: 9.81, playerSpeed: 5, bloomStrength: 0.5, debugPhysics: false };
const gui = new GUI({ title: 'Settings' });
gui.add(params, 'gravity', 0, 20, 0.1);
gui.add(params, 'playerSpeed', 1, 20, 0.5);
gui.add(params, 'bloomStrength', 0, 2, 0.05);
gui.add(params, 'debugPhysics');
```

## Screenshot Evaluation

| When | Capture | Check |
|---|---|---|
| Initial load | Title/menu | Fonts loaded? Layout correct? Debug overlay showing? |
| Gameplay | Active scene | FPS 50+? Entities rendering? No z-fighting? HUD readable? |
| Interactions | Post-action | State change visible? Particles? Score updated? |
| Edge cases | Game over, pause | Design system consistent? Typography matches tokens? |
| Both sizes | 1280px + 375px | Responsive? Touch targets adequate? |

Checklist per screenshot:
- Rendering correct — all elements present and positioned
- FPS 50+ (below 30 = failure)
- No visual glitches (z-fighting, clipping, pop-in)
- UI text readable over scene (contrast safety from `game.md`)
- Design tokens applied consistently
- Memory stable (not growing between screenshots)

For animation verification, take sequential screenshots at t=0, t=500ms, t=1000ms and compare.

## Performance Profiling

### Targets

| Metric | Target | Red Flag | Source |
|---|---|---|---|
| FPS | 60 | <30 | Debug overlay |
| Frame time | ≤16.67ms | >33ms | `performance.now()` delta |
| Draw calls | <100 mobile, <300 desktop | >500 | `renderer.info.render.calls` |
| Geometries | Stable | Growing | `renderer.info.memory.geometries` |
| Textures | Stable | Growing | `renderer.info.memory.textures` |
| JS Heap | Stable after warmup | Growing | `performance.memory` |

### renderer.info (Three.js)

Call `renderer.info.reset()` before rendering each frame — without it, counters accumulate across frames.

```javascript
function gameLoop() {
  requestAnimationFrame(gameLoop);
  renderer.info.reset();
  // ... update ...
  renderer.render(scene, camera);
  debug.update(); // reads per-frame stats
}
```

### CPU vs GPU Bottleneck

Halve canvas resolution (`renderer.setSize(w/2, h/2)`). FPS jumps → GPU-bound. No change → CPU-bound (game logic, physics, or draw calls).

### Memory Leak Detection

```javascript
setInterval(() => {
  const i = renderer.info;
  console.log(`[Mem] Geo:${i.memory.geometries} Tex:${i.memory.textures}`);
}, 10000);
```

If counts grow, you have a disposal leak. See Common Bugs below.

## Common Bugs

### Three.js Resource Disposal

Three.js does NOT garbage-collect GPU resources. Call `dispose()` on geometry, material, and textures when removing objects:

```javascript
function removeObject(obj) {
  obj.geometry?.dispose();
  const mats = Array.isArray(obj.material) ? obj.material : [obj.material].filter(Boolean);
  mats.forEach(m => { Object.values(m).forEach(v => v?.dispose?.()); m.dispose(); });
  obj.removeFromParent();
}
```

### Animation Frame Leaks

Always store the RAF ID: `rafId = requestAnimationFrame(animate)`. Cancel on cleanup: `cancelAnimationFrame(rafId)`.

### Event Listener Cleanup

Use `AbortController` for bulk removal:

```javascript
const ac = new AbortController();
window.addEventListener('resize', onResize, { signal: ac.signal });
window.addEventListener('keydown', onKey, { signal: ac.signal });
// Cleanup: ac.abort();
```

### Z-Fighting

Fixes in order: (1) offset geometry by 0.01 units, (2) tighten near/far planes (`near:0.1, far:1000` not `0.001/100000`), (3) `material.polygonOffset = true`, (4) logarithmic depth buffer (last resort).

### Audio Context

Resume on user gesture: `document.addEventListener('click', () => audioCtx.resume(), { once: true });`

### Physics Tunneling

Cap max velocity. Enable CCD in Rapier. Make collision bodies thicker than visual geometry.

### GC Stutters

Pre-allocate vectors/objects outside the game loop. Avoid `map()`, `filter()`, spread in hot paths. Use object pools for particles.

## Pre-Ship Checklist

**Performance:** 55+ fps avg · 30+ fps 1% low · draw calls <200 · stable memory · no GC stutters

**Visual:** All screens screenshotted · no artifacts · UI readable over all backgrounds · fonts loaded · design tokens consistent

**Functional:** All actions work · AI/NPC correct · score/health tracked · game-over triggers · audio plays · no console errors

**Sandbox:** Loads in iframe · no localStorage refs · all assets from CDN · controls work without Pointer Lock · fills viewport

**Cleanup:** RAF IDs stored · listeners removable · Three.js resources disposed · no orphaned timers

## Browser QA Companion

Read `.agents/skills/website-building/shared/12-playwright-interactive.md` before signoff. Use that guide for the browser-session workflow, observation posture, and screenshot discipline.

## Browser Tool Notes

- Prefer one browser session per QA pass instead of reopening between every check.
- Use `observe` to find stable element IDs before clicks or typing.
- Use `evaluate` for deterministic helpers such as `window.advanceTime(ms)` or `window.render_game_to_text()`, not as a replacement for real interaction.
- Capture screenshots only for states where visual evidence matters, then inspect them before signoff.

## References

- `.agents/skills/website-building/shared/12-playwright-interactive.md` — browser-tool workflow for observation, interaction, screenshots, and viewport checks.
- `window.advanceTime(ms)` and `window.render_game_to_text()` — deterministic hooks owned by the game under test, not substitutes for real user input.

