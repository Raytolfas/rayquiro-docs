---
title: fs
description: File system operations, file reading, writing, directory
  management, and file checks.
slug: 0.2.1/built-ins/fs
---

The `fs` namespace provides comprehensive synchronous file system operations. No import is required.

***

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `fs.read` | `fs.read(path)` | `string` | Reads an entire file as a UTF-8 string. |
| `fs.write` | `fs.write(path, content)` | `void` | Writes content to a file, overwriting existing data. |
| `fs.append` | `fs.append(path, content)` | `void` | Appends content to the end of a file. |
| `fs.exists` | `fs.exists(path)` | `bool` | Checks if a file or directory exists. |
| `fs.mkdir` | `fs.mkdir(path)` | `bool` | Creates a directory (including parent directories). |
| `fs.readdir` | `fs.readdir(path)` | `array` | Lists file and folder names inside a directory. |
| `fs.remove` | `fs.remove(path)` | `bool` | Deletes a file or directory. |
| `fs.copy` | `fs.copy(src, dest)` | `bool` | Copies a file from source to destination. |

***

## Detailed Methods

### `fs.read(path)`

Reads the full content of the file specified by `path`. Throws an exception if the file cannot be opened or does not exist.

```js
try {
    var content = fs.read("config.json");
    var config = json.parse(content);
    print("Database Host: " + config["host"]);
} catch (err) {
    print("Failed to read file: " + err);
}
```

***

### `fs.write(path, content)`

Writes string `content` into the file at `path`. If the file does not exist, it will be created. If parent directories do not exist, ensure you create them with `fs.mkdir`.

```js
var log_entry = "Session started at " + str(datetime.timestamp()) + "\n";
fs.write("logs/session.log", log_entry);
```

***

### `fs.append(path, content)`

Appends string data to an existing file without modifying previously written content.

```js
fs.append("events.csv", "user_signup,104,success\n");
```

***

### `fs.exists(path)`

Returns `true` if the specified file or folder exists on the disk, or `false` otherwise.

```js
if (fs.exists("savegame.dat")) {
    var save = fs.read("savegame.dat");
    print("Loaded save data: " + str(len(save)) + " bytes");
} else {
    print("No existing save file found. Initializing new game.");
}
```

***

### `fs.mkdir(path)`

Recursively creates all directories in the specified path. Returns `true` if the directory was created or already exists.

```js
fs.mkdir("build/output/assets");
```

***

### `fs.readdir(path)`

Scans the given directory and returns an array of strings representing the names of entries inside it.

```js
var files = fs.readdir("./assets");
var i = 0;
while (i < len(files)) {
    var filename = files[i];
    print("Found asset: " + filename);
    i = i + 1;
}
```

***

### `fs.remove(path)`

Removes a file or an empty directory. Returns `true` upon successful deletion.

```js
if (fs.exists("temp.tmp")) {
    fs.remove("temp.tmp");
}
```

***

### `fs.copy(src, dest)`

Copies a file from `src` to `dest`.

```js
fs.copy("assets/default_skin.png", "user_data/skin.png");
```
