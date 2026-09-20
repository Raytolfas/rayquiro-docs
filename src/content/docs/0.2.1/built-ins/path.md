---
title: path
description: Cross-platform file path manipulation, normalization, extension
  extraction, and joining.
slug: 0.2.1/built-ins/path
---

The `path` namespace ensures cross-platform consistency when working with file system paths on Windows, Linux, and macOS.

***

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `path.join` | `path.join(...parts)` | `string` | Combines path segments using the system separator. |
| `path.basename` | `path.basename(p)` | `string` | Returns the final portion of a path. |
| `path.dirname` | `path.dirname(p)` | `string` | Returns the directory name portion of a path. |
| `path.ext` | `path.ext(p)` | `string` | Extracts the extension (including leading `.`). |
| `path.stem` | `path.stem(p)` | `string` | Returns the file name without its extension. |
| `path.is_abs` | `path.is_abs(p)` | `bool` | Determines if a path is absolute. |
| `path.normalize` | `path.normalize(p)` | `string` | Resolves `.` and `..` segments and cleans separators. |

***

## Detailed Methods

### `path.join(...parts)`

Joins multiple path components safely using appropriate platform separators (`/` on Linux/macOS, `\\` on Windows):

```js
var full = path.join("data", "users", "profile.json");
print(full); // "data/users/profile.json" (Linux) or "data\\users\\profile.json" (Windows)
```

***

### `path.basename(path)`

Returns the last element of the path.

```js
print(path.basename("/home/user/project/main.rq")); // "main.rq"
print(path.basename("C:\\projects\\app.exe"));       // "app.exe"
```

***

### `path.dirname(path)`

Returns the directory path excluding the final file/folder component.

```js
print(path.dirname("/var/log/nginx/access.log")); // "/var/log/nginx"
```

***

### `path.ext(path)`

Returns the file extension.

```js
print(path.ext("archive.tar.gz")); // ".gz"
print(path.ext("document.pdf"));    // ".pdf"
print(path.ext("Makefile"));        // ""
```

***

### `path.stem(path)`

Returns the filename without its trailing extension.

```js
print(path.stem("archive.zip")); // "archive"
print(path.stem("game.exe"));    // "game"
```

***

### `path.is_abs(path)`

Checks whether the given path is absolute.

```js
print(path.is_abs("/usr/bin"));      // true (Linux/macOS)
print(path.is_abs("C:\\Windows"));   // true (Windows)
print(path.is_abs("src/main.rq"));   // false
```
