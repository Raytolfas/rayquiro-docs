---
title: Core API (rqio_core)
description: Embed RayQuiro into C++, C, C#, Python, and game engines using the native dynamic library rqio_core.dll / rqio_core.so.
---

`rqio_core` is the native shared library (`rqio_core.dll` on Windows, `rqio_core.so` on Linux, `rqio_core.dylib` on macOS) that exposes RayQuiro's runtime, VM, parser, and interpreter via a pure **C ABI**.

This allows you to embed the RayQuiro language into game engines (such as Raytolfas Engine, Unreal, Godot), desktop applications, C# / .NET runtimes, Python scripts, or custom microservices with zero overhead.

---

## C Header: `RqioCoreAPI.h`

The C interface is defined in `include/rayquiro/RqioCoreAPI.h`:

```c
#pragma once

#include <stddef.h>

#ifdef _WIN32
#define RQIO_CORE_EXPORT extern "C" __declspec(dllexport)
#else
#define RQIO_CORE_EXPORT extern "C"
#endif

typedef struct RqioCoreHandle RqioCoreHandle;

typedef enum RqioCoreStatus {
    RQIO_CORE_OK = 0,
    RQIO_CORE_ERROR = 1
} RqioCoreStatus;

RQIO_CORE_EXPORT const char* rqio_core_version(void);
RQIO_CORE_EXPORT int rqio_core_create(const char* project_root, const char* executable_path, RqioCoreHandle** out_handle, char** out_error);
RQIO_CORE_EXPORT void rqio_core_destroy(RqioCoreHandle* handle);
RQIO_CORE_EXPORT int rqio_core_set_project_root(RqioCoreHandle* handle, const char* project_root, char** out_error);
RQIO_CORE_EXPORT int rqio_core_set_executable_path(RqioCoreHandle* handle, const char* executable_path, char** out_error);
RQIO_CORE_EXPORT int rqio_core_run_file(RqioCoreHandle* handle, const char* script_path, int prefer_vm, int* out_exit_code, char** out_error);
RQIO_CORE_EXPORT int rqio_core_run_source(RqioCoreHandle* handle, const char* virtual_filename, const char* source_code, int prefer_vm, int* out_exit_code, char** out_error);
RQIO_CORE_EXPORT int rqio_core_describe_file(RqioCoreHandle* handle, const char* script_path, char** out_json, char** out_error);
RQIO_CORE_EXPORT int rqio_core_describe_source(RqioCoreHandle* handle, const char* virtual_filename, const char* source_code, char** out_json, char** out_error);
RQIO_CORE_EXPORT void rqio_core_free_string(char* value);
```

---

## Memory Management Rules

1. Any output string returned by `out_error` or `out_json` is allocated on the heap by `rqio_core`.
2. When you are finished using a string, you **must** call `rqio_core_free_string(str)` to release it.
3. Every handle created with `rqio_core_create` **must** be destroyed with `rqio_core_destroy(handle)`.

---

## Function Reference

### `rqio_core_version`
```c
const char* rqio_core_version(void);
```
Returns a static null-terminated C string with the current RayQuiro Core version (e.g. `"0.2.1"`). Do **not** free this pointer.

---

### `rqio_core_create`
```c
int rqio_core_create(
    const char* project_root,
    const char* executable_path,
    RqioCoreHandle** out_handle,
    char** out_error
);
```
Initializes a new isolated RayQuiro runtime environment.
* `project_root`: Directory used to resolve relative file paths, `rqio.json`, and `.rqio/packages`. Pass `NULL` or `""` for current directory.
* `executable_path`: Path of the host executable (used for finding bundled toolchains and modules). Pass `NULL` or `""` if not applicable.
* `out_handle`: Pointer receiving the created handle.
* `out_error`: Pointer receiving an allocated error message if creation fails.
* **Returns**: `RQIO_CORE_OK` (0) on success, or `RQIO_CORE_ERROR` (1) on failure.

---

### `rqio_core_destroy`
```c
void rqio_core_destroy(RqioCoreHandle* handle);
```
Destroys the runtime context and frees all associated memory, environments, and loaded modules.

---

### `rqio_core_run_file`
```c
int rqio_core_run_file(
    RqioCoreHandle* handle,
    const char* script_path,
    int prefer_vm,
    int* out_exit_code,
    char** out_error
);
```
Executes a RayQuiro script from disk.
* `script_path`: Absolute or relative path to the `.rq` or `.rqb` file.
* `prefer_vm`: Pass `1` to run via Bytecode VM, or `0` to run via Interpreter.
* `out_exit_code`: Pointer receiving the script return/exit code.
* `out_error`: Pointer receiving error message if an exception is thrown.
* **Returns**: `RQIO_CORE_OK` (0) or `RQIO_CORE_ERROR` (1).

---

### `rqio_core_run_source`
```c
int rqio_core_run_source(
    RqioCoreHandle* handle,
    const char* virtual_filename,
    const char* source_code,
    int prefer_vm,
    int* out_exit_code,
    char** out_error
);
```
Executes RayQuiro code directly from an in-memory string without writing to disk.
* `virtual_filename`: Virtual name used in stack traces and diagnostic messages (e.g. `"memory.rq"`).
* `source_code`: Null-terminated string containing RayQuiro code.
* `prefer_vm`: `1` for VM, `0` for Interpreter.

---

### `rqio_core_describe_source` / `rqio_core_describe_file`
```c
int rqio_core_describe_source(
    RqioCoreHandle* handle,
    const char* virtual_filename,
    const char* source_code,
    char** out_json,
    char** out_error
);
```
Inspects the source code without running it, returning a JSON string detailing AST compatibility, required native modules (`app`, `web`, `ui`, `engine`), and VM/interpreter support.
The returned JSON string must be freed with `rqio_core_free_string`.

---

### `rqio_core_free_string`
```c
void rqio_core_free_string(char* value);
```
Frees memory for strings allocated by `rqio_core`. Safe to call on `NULL`.