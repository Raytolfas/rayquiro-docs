---
title: process
description: Command-line arguments, process termination, working directory, and PID management.
---

The `process` namespace provides access to current OS process parameters and control.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `process.args` | `process.args()` | `array` | Returns command-line arguments passed to the script. |
| `process.exit` | `process.exit(code)` | `never` | Terminates the current process immediately with an exit code. |
| `process.cwd` | `process.cwd()` | `string` | Returns the current working directory path. |
| `process.pid` | `process.pid()` | `number` | Returns the unique process ID. |
| `process.chdir` | `process.chdir(dir)` | `bool` | Changes the current working directory. |

---

## Detailed Methods

### `process.args()`

Returns an array of strings containing arguments passed after the script filename.

```bash
rqio run cli_tool.rq --input data.txt --verbose
```

```js
// cli_tool.rq
var args = process.args();
print("Total arguments: " + str(len(args)));

var i = 0;
while (i < len(args)) {
    print("Arg " + str(i) + ": " + args[i]);
    i = i + 1;
}
```

---

### `process.exit(code = 0)`

Immediately halts execution of the script or compiled binary and returns the specified integer status code to the operating system.

- `0`: Success / normal exit.
- `1` or greater: Error / abnormal exit.

```js
var input_file = "data.csv";
if (!fs.exists(input_file)) {
    print("Error: Missing input file " + input_file);
    process.exit(1);
}
```

---

### `process.cwd()`

Returns an absolute path representing the process's current working directory.

```js
var current_dir = process.cwd();
print("Working in: " + current_dir);
```

---

### `process.pid()`

Returns the operating system Process ID (PID), useful for logging, creating lockfiles, or process supervision.

```js
var pid = process.pid();
print("Process ID: " + str(pid));
fs.write("server.pid", str(pid));
```