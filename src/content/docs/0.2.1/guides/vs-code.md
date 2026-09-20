---
title: VS Code Extension Guide
description: Installing, configuring, and using the official RayQuiro extension
  for Visual Studio Code.
slug: 0.2.1/guides/vs-code
---

The official RayQuiro VS Code extension provides syntax highlighting, auto-completion, code formatting, and interactive debugging directly inside your editor.

***

## 1. Installation

Install the `.vsix` extension package:

1. Download `rayquiro-0.2.0.vsix` from [GitHub Releases](https://github.com/raytolfas/rayquiro/releases).
2. In VS Code, open the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X`).
3. Click the `...` menu at the top of the Extensions view.
4. Select **Install from VSIX...** and choose the downloaded file.

***

## 2. Features

### Syntax Highlighting

Full syntax coloring for `.rq` files, including:

* Keywords (`fn`, `var`, `struct`, `import`, `while`, `if`, `return`, `throw`, `try`, `catch`, `finally`)
* Literals (numbers, strings, booleans, null)
* Operators (`??`, `?.`, `==`, `!=`, etc.)
* Built-in namespaces (`fs`, `json`, `datetime`, `crypto`, `engine`, `web`, `ui`)

***

### In-Editor Debugging (F5)

To debug a RayQuiro script:

1. Open your `.rq` file.
2. Set breakpoints by clicking in the left margin next to line numbers.
3. Press **F5** to start debugging.
4. The extension communicates directly with `rqio debug --port 4711`.
5. You can inspect local and global variables, step through lines (`F10`), step into functions (`F11`), and evaluate expressions in the Debug Console.

***

### Code Formatting

Format any document on save or by pressing `Shift+Alt+F` (Windows/Linux) or `Shift+Option+F` (macOS). The extension automatically invokes `rqio fmt`.
