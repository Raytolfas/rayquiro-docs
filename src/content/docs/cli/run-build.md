---
title: rqio run / build
description: Run scripts and compile standalone native binaries with LLVM.
---

## rqio run

Execute RayQuiro scripts directly using the high-performance Bytecode VM or legacy tree-walk interpreter.

```bash
rqio run <file.rq> [args...]
rqio run <file.rq> --legacy    # force tree-walk interpreter
```

Arguments passed after the script path are accessible within RayQuiro via `process.args()`.

---

## rqio build

Compile a RayQuiro script into a standalone, bare-metal native binary via **LLVM**. The compiled executable requires no external runtime or C++ dependencies.

```bash
rqio build <file.rq> [-o output] [flags...]
```

### Flags

| Flag | Description | Details |
|------|-------------|---------|
| `-o <path>` | Output binary path | Defaults to script name (`.exe` on Windows, no extension on Linux/macOS) |
| `--release` | Maximum performance | Enables `-O3` LLVM optimization passes |
| `--debug` | Debug build | Generates `-O0 -g` debug symbols for GDB / LLDB / VS Code |
| `--target <triple>` | Cross-compilation target | Target architecture and OS (e.g. `linux-x64`, `win-x64`, `macos-arm64`) |
| `--no-llvm` | GCC fallback | Forces compilation using GCC instead of LLVM/Clang |

### Target Aliases

The `--target` flag supports shorthand aliases as well as standard LLVM target triples:

| Alias | Target Triple | Target OS & Architecture |
|-------|---------------|--------------------------|
| `linux-x64` | `x86_64-unknown-linux-gnu` | Linux 64-bit (x86_64) |
| `linux-arm64` | `aarch64-unknown-linux-gnu` | Linux 64-bit ARM (AArch64) |
| `win-x64`, `windows-x64` | `x86_64-pc-windows-gnu` | Windows 64-bit (x86_64) |
| `macos-arm64`, `darwin-arm64` | `arm64-apple-darwin` | macOS Apple Silicon (M1/M2/M3) |
| `macos-x64`, `darwin-x64` | `x86_64-apple-darwin` | macOS 64-bit Intel |

### Examples

```bash
# Optimized compilation for host OS
rqio build app.rq -o app.exe

# Maximum release optimization with LLVM
rqio build game.rq --release -o game.exe

# Target Linux binary
rqio build server.rq --release --target linux-x64 -o server

# Debug build for stepping through with a debugger
rqio build script.rq --debug -o script_debug.exe
```
