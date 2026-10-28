---
title: rayquiro.engine
description: High-performance 2D and 3D game engine powered by Raylib OpenGL core with dynamic lighting, spatial audio, and camera systems.
---

The `rayquiro.engine` module is statically compiled into RayQuiro. Built upon the battle-tested Raylib OpenGL core, it provides guaranteed zero-configuration cross-platform windowing, hardware-accelerated 2D and 3D graphics, dynamic lighting with per-face normal shading and point lights, raycasting, camera systems, sound and music playback, and keyboard/mouse/gamepad input.

```js
import "rayquiro.engine";
```

---

## 1. Window & Engine Lifecycle

The engine uses **Raylib** as its primary, reliable foundation. It starts instantly without needing external graphics SDKs or complex driver setup.

| Method | Signature | Description |
|---|---|---|
| `engine.init` | `engine.init(width, height, title)` | Initializes rendering window and OpenGL context. |
| `engine.backend_name` | `engine.backend_name()` | Returns active backend name (default: `"raylib"`). |
| `engine.capabilities` | `engine.capabilities()` | Returns hardware and engine feature flags object. |
| `engine.should_close` | `engine.should_close()` | Returns `true` if window close button or Alt+F4 was triggered. |
| `engine.shutdown` | `engine.shutdown()` | Releases GPU resources, audio device, and window context. |
| `engine.frame_begin` | `engine.frame_begin(color)` | Clears frame buffers to specified background color. |
| `engine.frame_end` | `engine.frame_end()` | Finalizes rendering passes and presents the frame to display. |
| `engine.target_fps` | `engine.target_fps(fps)` | Locks frame rate (e.g. 60 or 144 FPS). |
| `engine.fps` | `engine.fps()` | Returns current frames per second counter. |
| `engine.frame_time` | `engine.frame_time()` | Delta time (`dt`) between frames in seconds. |

```js
import "rayquiro.engine";

engine.init(1280, 720, "RayQuiro 3D Engine");
engine.target_fps(60);

var caps = engine.capabilities();
print("Active backend:", engine.backend_name());
print("3D Supported:", caps["supports3D"]);
print("Raycasting:", caps["supportsRaycasting"]);
```

---

## 2. Dynamic Lighting System

The Raylib core supports real-time directional sunlight and dynamic point lights with distance quadratic attenuation and face normal shading:

| Method | Signature | Description |
|---|---|---|
| `engine.light_ambient` | `engine.light_ambient(r, g, b, [intensity])` | Sets ambient scene light color and intensity. |
| `engine.light_directional` | `engine.light_directional(dir, color, intensity)` | Sets directional sun vector, color, and intensity factor. |
| `engine.light_point` | `engine.light_point(id, pos, color, intensity, radius)` | Adds or updates dynamic point light with attenuation radius. |
| `engine.light_remove` | `engine.light_remove(id)` | Removes point light by identifier. |
| `engine.lights_clear` | `engine.lights_clear()` | Clears all dynamic point lights. |
| `engine.lights` | `engine.lights()` | Returns list of active point lights. |

```js
engine.lights_clear();
engine.light_ambient(28, 32, 44, 0.4);
engine.light_directional({"x": -0.4, "y": -1.0, "z": -0.3}, {"r": 255, "g": 240, "b": 220}, 1.2);
engine.light_point("torch", {"x": 0, "y": 2.5, "z": -5}, {"r": 255, "g": 180, "b": 60}, 2.0, 15.0);
```

---

## 3. Direct 3D Drawing Primitives

All 3D primitives are rendered with hardware depth-buffering and dynamic lighting:

### 3D Primitives
- `engine.draw_cube(pos, size, color)` — Solid 3D box with face normal shading and point light reception.
- `engine.draw_plane(pos, size, color)` — Horizontal 3D ground plane.
- `engine.draw_sphere(pos, radius, color)` — Shaded 3D sphere.
- `engine.draw_cylinder(pos, radius, height, color)` — Shaded 3D cylinder.
- `engine.draw_wire_cube(pos, size, color)` — 3D wireframe bounding box.
- `engine.draw_wire_sphere(pos, radius, color)` — 3D wireframe sphere.
- `engine.draw_line_3d(start, end, color)` — 3D line segment between two coordinates.
- `engine.draw_grid(slices, spacing)` — Ground reference grid.

### 3D Models & 2D Textures (glTF, OBJ, PNG, JPG)
- `engine.load_model(path)` — Loads 3D model file (`.glb`, `.gltf`, `.obj`) and returns model ID.
- `engine.unload_model(id)` — Releases 3D model and its meshes from GPU memory.
- `engine.draw_model(id, pos, scale, tint)` — Draws 3D model at position with scale and tint.
- `engine.draw_model_ex(id, pos, rot_axis, rot_angle, scale, tint)` — Draws 3D model with rotation axis, angle, scale vector, and tint.
- `engine.load_texture(path)` — Loads 2D texture (`.png`, `.jpg`) into GPU memory and returns texture ID.
- `engine.unload_texture(id)` — Unloads 2D texture from GPU memory.
- `engine.draw_texture(id, x, y, tint)` — Draws 2D texture at position `(x, y)` with tint color.
- `engine.draw_texture_ex(id, x, y, rot, scale, tint)` — Draws 2D texture with rotation angle, scale factor, and tint color.

### 2D Primitives & UI Overlays
- `engine.draw_rect(x, y, w, h, color)` — Filled 2D rectangle.
- `engine.draw_rect_lines(x, y, w, h, color)` — Outlined 2D rectangle.
- `engine.draw_circle(cx, cy, radius, color)` — Filled 2D circle.
- `engine.draw_circle_lines(cx, cy, radius, color)` — Outlined 2D circle.
- `engine.draw_line(x1, y1, x2, y2, color)` — 2D line segment.
- `engine.draw_pixel(x, y, color)` — Single pixel plot.
- `engine.draw_text(text, x, y, size, color)` — High-quality text rendering.
- `engine.draw_fps(x, y)` — Hardware FPS counter widget.

---

## 4. Camera Systems

| Method | Signature | Description |
|---|---|---|
| `engine.camera` | `engine.camera(pos, target, up, fov)` | Sets camera position, look target, up vector, and field of view. |
| `engine.camera_fps` | `engine.camera_fps(speed, sensitivity)` | Built-in first-person WASD and mouse look update. |
| `engine.camera_orbit` | `engine.camera_orbit(yaw, pitch, radiusDelta)` | Revolves camera around target point. |

```js
var px = 0.0;
var py = 1.7;
var pz = 10.0;
var fov = 75.0;

engine.camera(
    {"x": px, "y": py, "z": pz},
    {"x": 0.0, "y": 1.7, "z": 0.0},
    {"x": 0.0, "y": 1.0, "z": 0.0},
    fov
);
```

---

## 5. Input Handling

| Method | Signature | Description |
|---|---|---|
| `engine.key_down` | `engine.key_down(key)` | Returns `true` while key is held down (key code or letter string). |
| `engine.key_pressed` | `engine.key_pressed(key)` | Returns `true` once on the frame the key was pressed. |
| `engine.mouse_down` | `engine.mouse_down(button)` | Returns `true` if mouse button (0=left, 1=right) is held. |
| `engine.mouse_pos` | `engine.mouse_pos()` | Returns `[mouseX, mouseY]` array. |
| `engine.mouse_delta` | `engine.mouse_delta()` | Returns `{"dx": ..., "dy": ...}` mouse movement delta. |

```js
if (engine.key_down("W")) {
    pz = pz - speed * dt;
}

var mDelta = engine.mouse_delta();
yaw = yaw + mDelta["dx"] * sens;
```

---

## 6. Audio System (`audio.*`)

The engine includes integrated spatial and 2D audio processing:

| Function | Signature | Description |
|---|---|---|
| `audio.init` | `audio.init()` | Initializes the audio hardware device. |
| `audio.load_sound` | `audio.load_sound(path)` | Loads sound effect into memory (`.wav`, `.ogg`, `.mp3`). |
| `audio.play` | `audio.play(sound)` | Plays loaded sound effect. |
| `audio.stop` | `audio.stop(sound)` | Stops playing sound effect. |
| `audio.set_volume` | `audio.set_volume(sound, vol)` | Sets volume (`0.0` to `1.0`). |
| `audio.load_music` | `audio.load_music(path)` | Streams music track from file. |
| `audio.play_music` | `audio.play_music(music)` | Starts music streaming. |
| `audio.update_music` | `audio.update_music(music)` | Updates music stream buffers (call each frame). |

---

## 7. Complete 3D Scene Example

```js
import "rayquiro.engine";

var screenW = 1280;
var screenH = 720;
engine.init(screenW, screenH, "RayQuiro 3D - Raylib Engine");
engine.target_fps(60);

var px = 0.0;
var py = 2.0;
var pz = 8.0;
var rot = 0.0;

while (!engine.should_close()) {
    var dt = engine.frame_time();
    rot = rot + 45.0 * dt;

    engine.camera(
        {"x": px, "y": py, "z": pz},
        {"x": 0.0, "y": 1.0, "z": 0.0},
        {"x": 0.0, "y": 1.0, "z": 0.0},
        75.0
    );

    engine.lights_clear();
    engine.light_ambient(30, 36, 48, 0.4);
    engine.light_directional({"x": -0.5, "y": -1.0, "z": -0.3}, {"r": 255, "g": 240, "b": 220}, 1.2);
    engine.light_point("beacon", {"x": 0.0, "y": 3.0, "z": 0.0}, {"r": 80, "g": 200, "b": 255}, 2.0, 15.0);

    engine.frame_begin({"r": 16, "g": 18, "b": 24});

    engine.draw_grid(20, 1.0);
    engine.draw_cube({"x": 0.0, "y": -0.05, "z": 0.0}, {"x": 12.0, "y": 0.1, "z": 12.0}, {"r": 40, "g": 44, "b": 52});
    engine.draw_cube({"x": 0.0, "y": 1.0, "z": 0.0}, {"x": 1.6, "y": 2.0, "z": 1.6}, {"r": 220, "g": 60, "b": 60});
    engine.draw_wire_cube({"x": 0.0, "y": 1.0, "z": 0.0}, {"x": 2.2, "y": 2.6, "z": 2.2}, {"r": 255, "g": 255, "b": 255});
    engine.draw_cylinder({"x": 3.0, "y": 1.0, "z": 0.0}, 0.5, 2.0, {"r": 60, "g": 160, "b": 240});

    engine.draw_fps(16, 16);
    engine.draw_text("RayQuiro 3D Raylib Engine Active", 16, 40, 16, {"r": 255, "g": 255, "b": 255});

    engine.frame_end();
}

engine.shutdown();
```
