---
title: Creating Packages
description: Comprehensive step-by-step guide to developing, testing, and
  structuring reusable RayQuiro libraries.
slug: 0.2.1/packages/creating-packages
---

RayQuiro includes a built-in package system designed to make distributing and consuming reusable modules seamless, fast, and secure.

***

## 1. Package Directory Layout

A standard RayQuiro package follows this layout:

```text
my-math/
├── rqio.json              # Package manifest (metadata, dependencies, entry)
├── README.md              # Documentation, installation guide, and examples
├── LICENSE                # Open source license (MIT, Apache-2.0, etc.)
├── index.rq               # Primary library export entrypoint
└── src/
    ├── geometry.rq        # Internal sub-module
    ├── vector.rq          # Internal sub-module
    └── helpers.rq         # Helper utilities
```

***

## 2. Initializing a Package

To begin developing a package, create an empty directory and run `rqio init`:

```bash
mkdir my-math
cd my-math
rqio init
```

This creates a default `rqio.json` manifest:

```json
{
  "name": "my-math",
  "version": "1.0.0",
  "description": "Essential mathematical algorithms and vector utilities",
  "entry": "index.rq",
  "author": "Developer <dev@example.com>",
  "license": "MIT",
  "dependencies": {}
}
```

***

## 3. Writing Package Code

In `index.rq`, export public functions, structures, and classes. You can import other internal files relatively using `./`:

```js
// index.rq
import "./src/geometry.rq";
import "./src/vector.rq";

fn clamp(val, min_val, max_val) {
    if (val < min_val) { return min_val; }
    if (val > max_val) { return max_val; }
    return val;
}

fn lerp(a, b, t) {
    return a + (b - a) * t;
}

fn map_range(value, in_min, in_max, out_min, out_max) {
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
```

```js
// src/vector.rq
fn vec2(x, y) {
    return { x: x, y: y };
}

fn vec2_add(a, b) {
    return { x: a["x"] + b["x"], y: a["y"] + b["y"] };
}

fn vec2_dot(a, b) {
    return a["x"] * b["x"] + a["y"] * b["y"];
}
```

***

## 4. Declaring Dependencies

If your package relies on other packages, declare them in `rqio.json`:

```json
{
  "dependencies": {
    "telebot": "^2.1.0",
    "raytolfas/json-schema": "v1.0.0"
  }
}
```

Run `rqio install` to resolve and download dependencies into `.rqio/packages/`.

***

## 5. Testing Your Package Locally

To test your package locally inside another project before publishing:

```bash
cd /path/to/my-game
rqio add ../my-math --local
```

RayQuiro installs the local folder as a package in `.rqio/packages/my-math/`. In your application:

```js
import "my-math";

var pos = vec2(10, 20);
var delta = vec2(5, -2);
var new_pos = vec2_add(pos, delta);

print("New X: " + str(new_pos["x"])); // 15
print("New Y: " + str(new_pos["y"])); // 18
```

***

## 6. Guidelines & Best Practices

1. **Clear Entry Point:** Keep `index.rq` as the primary facade. Hide internal helpers inside `src/`.
2. **Strict SemVer:** Follow `MAJOR.MINOR.PATCH` increments. Breaking API changes must increment `MAJOR`.
3. **No External Binaries:** Rely on pure RayQuiro code or built-in modules (`fs`, `crypto`, `engine`, `web`, `ui`) whenever possible.
4. **Documentation:** Provide thorough descriptions and code snippets in `README.md`.
