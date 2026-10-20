---
title: os
description: Operating system inspection, host platform detection, paths, and
  environment checks.
slug: 1.0/built-ins/os
---

The `os` namespace provides metadata about the underlying host platform and operating system. No import is required.

***

## Quick Reference

| Function / Property | Signature | Return Type | Description |
|---------------------|-----------|-------------|-------------|
| `os.name` | `os.name()` | `string` | Returns host OS name (`"windows"`, `"linux"`, `"macos"`). |
| `os.arch` | `os.arch()` | `string` | Returns processor architecture (`"x86_64"`, `"x86"`, `"arm64"`, `"arm"`). |
| `os.cwd` | `os.cwd()` | `string` | Returns current working directory path. |
| `os.chdir` | `os.chdir(path)` | `bool` | Changes current working directory. Returns `true` on success. |
| `os.home` | `os.home()` | `string` | Returns current user's home directory path. |
| `os.temp` | `os.temp()` | `string` | Returns system temporary directory path. |
| `os.sep` | `os.sep()` | `string` | Returns filesystem path separator (`\` on Windows, `/` on Linux/macOS). |
| `os.exists` | `os.exists(path)` | `bool` | Checks if path exists on disk. |
| `os.is_dir` | `os.is_dir(path)` | `bool` | Returns `true` if path exists and is a directory. |
| `os.is_file` | `os.is_file(path)` | `bool` | Returns `true` if path exists and is a regular file. |

***

## Detailed Methods

### `os.name()` and `os.arch()`

Detect operating system and CPU architecture for cross-platform logic:

```js
var platform = os.name();
var arch = os.arch();

print("Running on: " + platform + " (" + arch + ")");

if (platform == "windows") {
    print("Windows initialization...");
} else if (platform == "linux") {
    print("Linux initialization...");
} else {
    print("POSIX / Unix initialization...");
}
```

***

### `os.cwd()` and `os.chdir(path)`

Inspect and modify the current working directory of the process:

```js
print("Current dir: " + os.cwd());

if (os.chdir("..")) {
    print("Moved to parent dir: " + os.cwd());
}
```

***

### `os.home()` and `os.temp()`

Get system directories in a cross-platform manner:

```js
var userHome = os.home();
var tmpDir = os.temp();

print("User home: " + userHome);
print("Temporary directory: " + tmpDir);
```

***

### `os.exists(path)`, `os.is_dir(path)`, `os.is_file(path)`

Path validation and inspection:

```js
var target = path.join(os.home(), ".config");

if (os.exists(target)) {
    if (os.is_dir(target)) {
        print(".config is a directory");
    } else if (os.is_file(target)) {
        print(".config is a file");
    }
}
```
