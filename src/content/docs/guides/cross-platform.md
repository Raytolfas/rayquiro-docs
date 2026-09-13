---
title: Cross-Platform Guide
description: Writing portable RayQuiro applications across Windows, Linux, and macOS.
---

RayQuiro was engineered from the ground up for strict cross-platform compatibility across Windows, Linux, and macOS.

---

## 1. Cross-Platform Core Guidelines

### 1. File Paths

Never hardcode path separators (`\\` or `/`). Always use `path.join`:

```js
// Cross-platform:
var config_path = path.join(process.cwd(), "config", "settings.json");

// Avoid:
// var bad_path = "config\\settings.json";
```

---

### 2. Platform Detection

Use `os.platform()` and `os.arch()` to conditionally handle platform-specific tasks:

```js
if (os.platform() == "windows") {
    print("Running on Windows");
} else if (os.platform() == "linux") {
    print("Running on Linux");
} else if (os.platform() == "macos") {
    print("Running on macOS");
}
```

---

### 3. Cross-Compiling with LLVM

You can cross-compile RayQuiro applications from your development machine to target other operating systems using the `--target` flag:

```bash
# Build for Linux (ELF 64-bit):
rqio build app.rq --target linux-x64 -o app_linux

# Build for Windows (.exe):
rqio build app.rq --target win-x64 -o app.exe

# Build for Apple Silicon macOS:
rqio build app.rq --target macos-arm64 -o app_macos
```

---

## 2. Platform Installation Methods

| Operating System | Automated Installer |
|------------------|---------------------|
| **Windows** | `irm rq.raytolfas.cc | iex` (PowerShell) |
| **Linux** | `curl -fsSL rq.raytolfas.cc/linux | bash` |
| **macOS** | `curl -fsSL rq.raytolfas.cc/mac | bash` |