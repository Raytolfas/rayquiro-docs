---
title: Formatting, Debugging & Utility CLI
description: Reference for rqio fmt, debug (DAP server), self-update, and version commands.
---

RayQuiro includes developer tooling directly inside the `rqio` binary.

---

## 1. Code Formatter (`rqio fmt`)

Format RayQuiro source files in place with standard indentation and formatting conventions:

```bash
rqio fmt main.rq
rqio fmt src/*.rq
```

The formatter normalizes:
- 4-space indentation
- Consistent brace placement `{}`
- Operator spacing (`a + b`, `x == y`)
- Comma and semicolon spacing

---

## 2. VS Code Debugger Server (`rqio debug`)

RayQuiro includes a built-in **Debug Adapter Protocol (DAP)** server that connects directly with VS Code, Neovim, or any DAP-compatible editor:

```bash
rqio debug main.rq --port 4711
```

### Features Supported:
- Breakpoints and conditional breakpoints
- Step Over, Step Into, Step Out
- Local and global variable inspection
- Call stack traces
- Console evaluate expressions

In VS Code with the official RayQuiro extension, pressing **F5** automatically launches this debug server.

---

## 3. Self-Update (`rqio self-update`)

Check for and install updates to the RayQuiro toolchain directly from GitHub Releases:

```bash
# Check if a newer version is available:
rqio self-update check

# Download and apply the latest release:
rqio self-update
```

---

## 4. Syntax & AST Validation (`rqio check`)

Verify syntax and build AST without executing the code:

```bash
rqio check main.rq
```

Outputs `[PASS] main.rq syntax and AST validated successfully.` or prints parse errors with file, line, and column info.

---

## 5. Built-in C Compiler Toolchain (`rqio cc`)

RayQuiro 1.0 bundles an integrated TinyCC compiler toolchain, allowing you to compile C files or link native code directly without installing external compilers:

```bash
rqio cc main.c -o app.exe
rqio cc -v
```

---

## 6. Version & Help

```bash
# Print current version:
rqio version
# or: rqio --version

# Print interactive help menu:
rqio help
```