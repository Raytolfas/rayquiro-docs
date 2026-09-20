---
title: rqio run / build / repl
description: Run scripts, hot reload, interactive REPL, and compile standalone
  native binaries with TinyCC and LLVM.
slug: 0.2.1/cli/run-build
---

## rqio run

Execute RayQuiro scripts directly using the high-performance Bytecode VM or tree-walk interpreter.

```bash
rqio run <file.rq> [args...]
rqio run <file.rq> --watch        # Hot Reload: automatically reloads on file save
rqio run <file.rq> --legacy       # Force tree-walk interpreter
```

### Hot Reload (`--watch` / `-w`)

When the `--watch` flag is passed, `rqio` keeps running and continuously monitors the script file. Every time you save changes to the file, the runtime immediately reloads and executes the updated code without restarting your terminal.

```bash
rqio run app.rq --watch
```

Arguments passed after the script path are accessible within RayQuiro via `process.args()`.

***

## rqio repl

Launch the interactive RayQuiro REPL (Read-Eval-Print Loop) shell:

```bash
rqio repl
rqio           # Running rqio without arguments in a non-project folder also opens REPL
```

In the REPL, you can type expressions, test built-in packages, define functions, and inspect values interactively:

```text
RayQuiro 0.2.1 REPL
Type "exit" or press Ctrl+C to quit.

>>> var x = random.int(1, 100)
>>> x * 2
84
>>> fn greet(name) { return "Hello, " + name + "!" }
>>> greet("RayQuiro")
"Hello, RayQuiro!"
>>> exit
```

***

## rqio build

Compile a RayQuiro script into a standalone, bare-metal native binary. The compiled executable has zero external runtime or VM dependencies.

```bash
rqio build <file.rq> [-o output] [flags...]
```

### Supported Compilers

RayQuiro 0.2.1 includes autonomous compiler support:

1. **TinyCC (TCC)**: Bundled directly with RayQuiro (`tools/tcc/` on Windows, system `tcc` on Linux). Enables fast, zero-dependency autonomous native compilation without requiring Clang, LLVM, or GCC installed on the machine.
2. **LLVM / Clang**: For aggressive compiler optimizations and cross-compilation.

### Flags

| Flag | Description | Details |
|------|-------------|---------|
| `-o <path>` | Output binary path | Defaults to script name (`.exe` on Windows, no extension on Linux/macOS) |
| `--tcc` | Autonomous TinyCC | Compiles within ~10ms using the bundled TinyCC toolchain (default for normal builds) |
| `--llvm` | Clang / LLVM | Compiles via LLVM Clang |
| `--release` | Maximum performance | Enables `-O3` LLVM optimization passes (falls back to TCC if Clang is unavailable) |
| `--debug` | Debug build | Generates `-O0 -g` debug symbols for GDB / LLDB / VS Code |
| `--target <triple>` | Cross-compilation target | Target architecture and OS (e.g. `linux-x64`, `win-x64`, `macos-arm64`) |
| `--no-llvm` | GCC fallback | Forces compilation using GCC instead of LLVM/Clang |

### Target Aliases

The `--target` flag supports shorthand aliases as well as standard LLVM target triples:

| Alias | Target Triple | Target OS & Architecture |
|-------|---------------|--------------------------|
| `linux-x64` | `x86_64-unknown-linux-gnu` | Linux 64-bit (x86\_64) |
| `linux-arm64` | `aarch64-unknown-linux-gnu` | Linux 64-bit ARM (AArch64) |
| `win-x64`, `windows-x64` | `x86_64-pc-windows-gnu` | Windows 64-bit (x86\_64) |
| `macos-arm64`, `darwin-arm64` | `arm64-apple-darwin` | macOS Apple Silicon (M1/M2/M3) |
| `macos-x64`, `darwin-x64` | `x86_64-apple-darwin` | macOS 64-bit Intel |

### Examples

```bash
# Autonomous build via TinyCC (no external compiler required)
rqio build app.rq -o app.exe

# Explicitly use TinyCC
rqio build math.rq --tcc -o math.exe

# Maximum release optimization with LLVM
rqio build game.rq --release -o game.exe

# Cross-compile for Linux x86_64
rqio build server.rq --release --target linux-x64 -o server

# Debug build for stepping through with a debugger
rqio build script.rq --debug -o script_debug.exe
```
