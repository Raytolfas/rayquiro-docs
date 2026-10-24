---
title: Modules System
description: Reference for RayQuiro modules, imports, native extensions, and standard namespaces.
---

RayQuiro features a modular, high-performance module architecture designed to combine the simplicity of dynamic scripting with the power and zero-dependency portability of native C/C++ runtimes.

---

## 1. Module Architecture Overview

In RayQuiro, modules are categorized into four distinct layers:

```
┌──────────────────────────────────────────────────────────┐
│                   Your RayQuiro Script                   │
└────────────┬─────────────┬─────────────┬─────────────────┘
             │             │             │
      ┌──────▼──────┐┌─────▼───────┐┌────▼────────┐
      │  Framework  ││  Standard   ││ User Files  │
      │   Modules   ││ Namespaces  ││ & Packages  │
      │ (rayquiro.*)││ (fs, json..)││  (local.rq) │
      └──────┬──────┘└─────┬───────┘└────┬────────┘
             │             │             │
┌────────────▼─────────────▼─────────────▼─────────────────┐
│           RayQuiro Core Engine & Runtime ABI             │
│      (Embedded C++ Engine, Raylib, TinyCC, Native OS)    │
└──────────────────────────────────────────────────────────┘
```

| Layer | Examples | How to Use | Runtime Dependency |
|-------|----------|------------|-------------------|
| **Framework Modules** | `rayquiro.app`, `rayquiro.ui`, `rayquiro.engine`, `rayquiro.web` | `import "rayquiro.app";` | Built directly into the `rqio` binary (zero external DLLs needed) |
| **Standard Namespaces** | `fs`, `path`, `json`, `datetime`, `crypto`, `hash`, `process`, `env`, `math`, `audio` | Globally available everywhere | Built-in, no import required |
| **Local Script Modules** | `./helpers.rq`, `../math/vector.rq` | `import "./helpers.rq";` | Resolved at parse time |
| **Package Manager Packages** | Installed via `rqio add <name>` | `import "package_name";` | Managed in `.rqio/packages` |

---

## 2. The `import` Syntax

RayQuiro provides flexible import statements for loading modules and selective symbols.

### Full Module Import

Imports the entire module namespace under its canonical identifier:

```rq
import "rayquiro.app";
import "rayquiro.ui";

var win = app.window({ title: "My App", width: 800, height: 600 });
var theme = ui.theme("nord");
```

### Selective Named Imports (`from ... import`)

Pulls specific functions, classes, or constants directly into the current scope:

```rq
from "rayquiro.ui" import theme, rgb, button_style;
from "rayquiro.app" import window;

var palette = theme("dracula");
var accent = rgb(255, 128, 0);
var btnStyle = button_style("danger");
```

### Local File Imports

You can split your project into multiple `.rq` source files using relative or absolute paths:

```rq
import "./config.rq";
import "../utils/math_helpers.rq";
```

All functions and global variables declared in the imported file become accessible in the importing script.

---

## 3. The 4 Built-in Framework Modules (`rayquiro.*`)

RayQuiro includes four specialized native framework modules. Unlike traditional scripting languages that require separate pip/npm installations and external shared libraries, all four framework modules are **compiled directly into the `rqio` binary**:

### 1. `rayquiro.app` — Window Management & App Lifecycle
Manages desktop windows, event queues, OS message pumps, and native window configurations.
- Window creation, resizing, title updates, and destruction.
- Event polling (`window.isOpen()`, `window.pollEvents()`).
- Process termination (`app.quit()`).
- [Read full `rayquiro.app` documentation →](/modules/app/)

### 2. `rayquiro.ui` — Styling, Theming & Design System
Provides styling presets, themes, CSS stylesheet parsing, and color manipulation. It works alongside `rayquiro.app` or game engines.
- Built-in themes: Dark, Light, Nord, Dracula, Cyberpunk, Midnight.
- Color algorithms: `rgb`, `rgba`, `hex`, `blend`, `lighten`, `darken`, `alpha`.
- Component styles: `button_style`, `card_style`, `text_style`, `badge_style`, `input_style`.
- CSS parser and serializer: `ui.parse(...)`, `ui.stringify(...)`, `ui.style(...)`.
- [Read full `rayquiro.ui` documentation →](/modules/ui/)

### 3. `rayquiro.engine` — 2D/3D Game Engine (Raylib Core)
Hardware-accelerated rendering, dynamic 3D lighting, spatial audio playback, camera controls, gizmos, and game loop management.
- Window rendering and draw callbacks (`engine.begin_drawing()`, `engine.draw_rect()`).
- Audio system (`audio.play_sound()`, `audio.play_music()`).
- Scene serialization and camera management.
- [Read full `rayquiro.engine` documentation →](/modules/engine/)

### 4. `rayquiro.web` — High-Performance Embedded HTTP Server
Micro-web framework and REST API engine.
- HTTP routing (`app.get()`, `app.post()`, `app.put()`, `app.delete()`).
- Request inspection (`req.path`, `req.headers`, `req.query`, `req.body`).
- Response serialization (`res.json()`, `res.html()`, `res.send()`).
- Static file serving (`app.static()`).
- [Read full `rayquiro.web` documentation →](/modules/web/)

---

## 4. `rayquiro.app` vs `rayquiro.ui`

A common question when developing desktop applications in RayQuiro is the role separation between `app` and `ui`:

```
┌──────────────────────────────────────────────────────────┐
│                   Desktop Application                    │
├────────────────────────────┬─────────────────────────────┤
│       rayquiro.app         │        rayquiro.ui          │
│   (Window & OS Lifecycle)  │   (Design System & Styles)  │
├────────────────────────────┼─────────────────────────────┤
│ • Window handle & HWND     │ • Color palettes & themes   │
│ • Window dimensions & pos  │ • CSS stylesheet parser     │
│ • OS Event polling loop    │ • Button & Card styling     │
│ • Minimize/Maximize/Close  │ • Typography & fonts        │
│ • Native message boxes     │ • Color blend / opacity     │
└────────────────────────────┴─────────────────────────────┘
```

### Cooperation Example

```rq
import "rayquiro.app";
import "rayquiro.ui";

var theme = ui.theme("nord");
var btnStyle = ui.button_style("primary", {
    "background": theme["primary"],
    "radius": 12
});

var win = app.window({
    title: "Themed Application",
    width: 800,
    height: 600,
    resizable: true
});

print("Window opened with theme: " + theme["name"]);
print("Button accent: " + btnStyle["background"]);

while (win.isOpen()) {
    win.pollEvents();
}
```

---

## 5. Standard Library Namespaces

The standard namespaces do not need an `import` declaration; they are automatically populated in the global environment:

| Namespace | Key Capabilities | Guide |
|-----------|------------------|-------|
| `fs` | `fs.read`, `fs.write`, `fs.exists`, `fs.mkdir`, `fs.readdir`, `fs.remove` | [File System →](/built-ins/fs/) |
| `path` | `path.join`, `path.basename`, `path.dirname`, `path.ext`, `path.stem`, `path.abs` | [Path →](/built-ins/path/) |
| `json` | `json.parse`, `json.stringify` | [JSON →](/built-ins/json/) |
| `datetime` | `datetime.now`, `datetime.timestamp`, `datetime.format` | [DateTime →](/built-ins/datetime/) |
| `crypto` | `crypto.sha256`, `crypto.uuid`, `crypto.random_bytes`, `crypto.hmac_sha256` | [Crypto →](/built-ins/crypto/) |
| `process` | `process.args`, `process.exit`, `process.cwd`, `process.pid` | [Process →](/built-ins/process/) |
| `env` | `env.get`, `env.set`, `env.has`, `env.all` | [Environment →](/built-ins/env/) |
| `math` | `sqrt`, `abs`, `pow`, `sin`, `cos`, `tan`, `log`, `min`, `max`, `pi` | [Standard Library →](/built-ins/standard-library/) |
| `audio` | `audio.play_sound`, `audio.play_music`, `audio.load_sound` | [Engine Audio →](/modules/engine/) |

---

## 6. Native ABI & Static Linking

When you distribute a RayQuiro application or run it with `rqio run` or compile it with `rqio build --release`:
1. **Zero External DLL Hell**: All C++ framework modules are built directly into the RayQuiro core. You do not need to ship separate C libraries or configure `LD_LIBRARY_PATH` / Windows `PATH`.
2. **Standard C ABI Dispatch**: Modules communicate via a high-speed JSON-buffered C ABI (`rqm_builtin_*_invoke`), providing strict boundary separation and instant cross-platform compatibility between Windows, Linux, and custom OS environments.
3. **No Network Dependency**: All framework modules work 100% offline.
