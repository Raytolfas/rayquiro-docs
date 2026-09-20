---
title: rqio.json Reference
description: Complete specification for the RayQuiro project manifest and
  package configuration file.
slug: 0.2.1/packages/rqio-json
---

The `rqio.json` file describes metadata, entry points, dependencies, build settings, and automation scripts for RayQuiro packages and applications.

***

## Schema Example

```json
{
  "name": "my-game",
  "version": "1.0.0",
  "description": "2D arcade game built with RayQuiro Engine",
  "author": "Raytolfas <contact@raytolfas.cc>",
  "license": "MIT",
  "entry": "main.rq",
  "build": {
    "output": "bin/game",
    "release": true,
    "target": "windows-x64"
  },
  "dependencies": {
    "telebot": "^2.1.0",
    "username/math-lib": "v1.0.0"
  },
  "devDependencies": {
    "rq-test": "^0.5.0"
  },
  "scripts": {
    "start": "rqio run main.rq",
    "build": "rqio build main.rq --release",
    "build:linux": "rqio build main.rq --release --target linux-x64 -o bin/game_linux",
    "test": "rqio run tests/test_all.rq"
  }
}
```

***

## Field Specifications

### Core Metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `string` | **Yes** | Unique package name. Lowercase alphanumeric with `-` or `_`. |
| `version` | `string` | **Yes** | Semantic version string: `MAJOR.MINOR.PATCH` (e.g. `1.0.0`). |
| `description` | `string` | No | Short human-readable summary of the package. |
| `entry` | `string` | **Yes** | Main script file executed upon import (defaults to `main.rq` or `index.rq`). |
| `author` | `string` | No | Author name and contact information. |
| `license` | `string` | No | Open-source license (e.g. `MIT`, `Apache-2.0`, `GPL-3.0`). |

***

### Dependencies (`"dependencies"`)

Specifies packages required at runtime:

```json
"dependencies": {
  "my-lib": "^1.2.0",
  "username/custom-tool": "v2.0.1"
}
```

* `"^1.2.0"`: Compatible semantic version (same major version).
* `"v1.0.0"`: Exact Git tag match.

***

### Build Options (`"build"`)

Configures default compilation settings for `rqio build`:

| Key | Type | Description |
|-----|------|-------------|
| `output` | `string` | Default output binary path. |
| `release` | `boolean` | Activates `-O3` LLVM optimization passes. |
| `target` | `string` | Target triple: `linux-x64`, `windows-x64`, `macos-arm64`. |
| `noLLVM` | `boolean` | Fallback to GCC compiler if true. |

***

### Custom Scripts (`"scripts"`)

Project tasks runnable via `rqio run <script>`:

```json
"scripts": {
  "dev": "rqio run main.rq",
  "build:prod": "rqio build main.rq --release -o bin/app.exe"
}
```
