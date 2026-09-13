---
title: os
description: Operating system inspection, host platform detection, and CPU architecture.
---

The `os` namespace provides metadata about the underlying host platform and operating system.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `os.platform` | `os.platform()` | `string` | Returns host OS name (`"windows"`, `"linux"`, `"macos"`). |
| `os.arch` | `os.arch()` | `string` | Returns processor architecture (`"x86_64"`, `"arm64"`). |
| `os.hostname` | `os.hostname()` | `string` | Returns computer network name. |
| `os.homedir` | `os.homedir()` | `string` | Returns current user home directory. |

---

## Example

```js
print("Running on: " + os.platform());
print("Architecture: " + os.arch());
print("Host: " + os.hostname());

if (os.platform() == "windows") {
    print("Windows specific initialization...");
} else {
    print("POSIX initialization...");
}
```