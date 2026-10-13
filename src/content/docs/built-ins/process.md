---
title: process
description: Command-line arguments, process termination, execution of external commands, working directory, and PID.
---

The `process` namespace provides access to current OS process parameters, child process execution, and process control. No import is required.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `process.args` | `process.args()` | `array` | Returns command-line arguments passed to the script. |
| `process.exit` | `process.exit(code = 0)` | `never` | Terminates the current process immediately with an exit code. |
| `process.cwd` | `process.cwd()` | `string` | Returns the current working directory path. |
| `process.pid` | `process.pid()` | `number` | Returns the unique operating system process ID. |
| `process.run` | `process.run(cmd)` | `string` | Executes a shell command synchronously and returns its stdout. |
| `process.exe_dir` | `process.exe_dir()` | `string` | Returns the directory containing the running executable. |

---

## Detailed Methods

### `process.args()`

Returns an array of strings containing arguments passed after the script filename:

```bash
rqio run cli_tool.rq --input data.txt --verbose
```

```js
var args = process.args();
print("Total arguments: " + str(len(args)));

var i = 0;
while (i < len(args)) {
    print("Arg " + str(i) + ": " + args[i]);
    i = i + 1;
}
```

---

### `process.run(command)`

Executes a command in the system shell and captures its text output:

```js
var gitCommit = process.run("git rev-parse --short HEAD");
print("Current Git commit: " + gitCommit);
```

---

### `process.exit(code = 0)`

Immediately halts execution of the script and returns the status code to the OS:

```js
var inputFile = "config.json";
if (!fs.exists(inputFile)) {
    print("Error: Missing " + inputFile);
    process.exit(1);
}
```

---

### `process.pid()` and `process.exe_dir()`

```js
var pid = process.pid();
var dir = process.exe_dir();

print("Process ID: " + str(pid));
print("Binary directory: " + dir);
```