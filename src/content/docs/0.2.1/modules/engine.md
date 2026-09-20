---
title: rayquiro.engine
description: Complete 2D and 3D multimedia game engine with Vulkan and Raylib renderers.
slug: 0.2.1/modules/engine
---

The `rayquiro.engine` module is statically compiled into RayQuiro. It provides windowing, hardware-accelerated 2D/3D graphics (via Vulkan or Raylib), sound/music playback, texture loading, font rendering, and keyboard/mouse/gamepad input.

```js
import "rayquiro.engine";
```

***

## 1. Window & Lifecycle Methods

| Method | Signature | Description |
|--------|-----------|-------------|
| `engine.init` | `engine.init(width, height, title)` | Initializes rendering window and OpenGL/Vulkan context. |
| `engine.shouldClose` | `engine.shouldClose()` | Returns `true` if the window close button or Alt+F4 was pressed. |
| `engine.close` | `engine.close()` | Frees engine resources and destroys the window. |
| `engine.setFps` | `engine.setFps(target_fps)` | Locks frame rate (e.g. 60 or 144 FPS). |
| `engine.getFps` | `engine.getFps()` | Returns current frames per second counter. |
| `engine.getFrameTime`| `engine.getFrameTime()` | Delta time (`dt`) between frames in seconds. |
| `engine.beginDraw` | `engine.beginDraw()` | Prepares the screen buffer for drawing. |
| `engine.endDraw` | `engine.endDraw()` | Flips double-buffers and presents the frame. |
| `engine.clear` | `engine.clear(r, g, b)` | Clears the background to an RGB color (`0..255`). |

***

## 2. 2D Drawing Primitives

| Method | Signature | Description |
|--------|-----------|-------------|
| `engine.drawRect` | `engine.drawRect(x, y, w, h, r, g, b)` | Draws a solid filled rectangle. |
| `engine.drawRectLines` | `engine.drawRectLines(x, y, w, h, r, g, b)` | Draws an outlined rectangle. |
| `engine.drawCircle` | `engine.drawCircle(cx, cy, radius, r, g, b)` | Draws a solid filled circle. |
| `engine.drawLine` | `engine.drawLine(x1, y1, x2, y2, r, g, b)` | Draws a line segment between two points. |
| `engine.drawText` | `engine.drawText(text, x, y, size, r, g, b)` | Renders text at coordinates with font size. |

***

## 3. Input Handling

### Keyboard Input

```js
if (engine.isKeyDown(262)) { // KEY_RIGHT
    player_x = player_x + speed * dt;
}
if (engine.isKeyPressed(32)) { // KEY_SPACE
    player_vy = -350.0; // Jump
}
```

### Mouse Input

```js
var mouse_pos = engine.getMousePosition(); // returns {x: ..., y: ...}
var left_clicked = engine.isMouseButtonPressed(0);
```

***

## 4. Audio & Textures

```js
// Textures
var sprite = engine.loadTexture("assets/player.png");
engine.drawTexture(sprite, 100, 150);
engine.drawTextureEx(sprite, 100, 150, 45.0, 2.0); // angle, scale

// Audio
var jump_sfx = engine.loadSound("assets/jump.wav");
engine.playSound(jump_sfx);

var bgm = engine.loadMusic("assets/theme.ogg");
engine.playMusic(bgm);
engine.updateMusic(bgm); // call once per frame in your loop
```

***

## 5. Complete Game Example

```js
import "rayquiro.engine";

engine.init(800, 600, "RayQuiro Pong");
engine.setFps(60);

var ball_x = 400.0;
var ball_y = 300.0;
var speed_x = 250.0;
var speed_y = 200.0;

while (!engine.shouldClose()) {
    var dt = engine.getFrameTime();

    // Physics
    ball_x = ball_x + speed_x * dt;
    ball_y = ball_y + speed_y * dt;

    if (ball_x < 10 || ball_x > 790) { speed_x = -speed_x; }
    if (ball_y < 10 || ball_y > 590) { speed_y = -speed_y; }

    // Render
    engine.beginDraw();
    engine.clear(20, 24, 32);

    engine.drawCircle(ball_x, ball_y, 12, 255, 100, 100);
    engine.drawText("FPS: " + str(engine.getFps()), 10, 10, 20, 200, 200, 200);

    engine.endDraw();
}

engine.close();
```
