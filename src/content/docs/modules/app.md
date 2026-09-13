---
title: rayquiro.app
description: Native desktop window management and application lifecycle for RayQuiro.
---

The `rayquiro.app` module provides direct integration with the operating system window manager, enabling desktop utilities, native alerts, system trays, and window event handling.

```js
import "rayquiro.app";
```

---

## 1. Quick Reference

| Method | Signature | Description |
|--------|-----------|-------------|
| `app.window` | `app.window(config)` | Creates and displays a native window. |
| `app.quit` | `app.quit()` | Signals the application message loop to exit. |
| `window.isOpen` | `window.isOpen()` | Returns true while the window has not been closed by the user. |
| `window.pollEvents` | `window.pollEvents()` | Dispatches pending OS events (mouse, keyboard, redraw). |
| `window.setTitle` | `window.setTitle(title)` | Dynamically changes the window title. |
| `window.setSize` | `window.setSize(w, h)` | Resizes the client area. |
| `window.close` | `window.close()` | Destroys the window handle. |

---

## 2. Window Configuration Options

```js
var win = app.window({
    title: "My Native App",
    width: 1024,
    height: 768,
    resizable: true,
    fullscreen: false,
    vsync: true
});
```

---

## 3. Desktop Application Lifecycle Example

```js
import "rayquiro.app";

var window = app.window({
    title: "System Monitor",
    width: 640,
    height: 480,
    resizable: false
});

var frame_count = 0;

while (window.isOpen()) {
    window.pollEvents();

    frame_count = frame_count + 1;
    if (frame_count % 60 == 0) {
        window.setTitle("System Monitor - Uptime: " + str(frame_count / 60) + "s");
    }

    time.sleep(16); // ~60 FPS
}

print("Application closed gracefully.");
```