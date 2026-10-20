---
title: ffi
description: Foreign Function Interface for loading dynamic shared libraries (.dll, .so) and calling C-ABI functions directly from RayQuiro.
---

The `ffi` module provides foreign function interface capabilities, allowing RayQuiro programs to load native shared libraries and invoke C functions directly with automatic conversion of primitives, strings, and byte buffers.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `ffi.load` | `ffi.load(path)` | `FFILibrary` | Loads a dynamic shared library (`.dll` on Windows, `.so` on POSIX). |
| `ffi.sym` | `ffi.sym(lib, name)` | `bool` | Checks whether a exported symbol exists in the loaded library. |
| `ffi.call` | `ffi.call(lib, name, ...args)` | `number` | Invokes an exported C function with up to 6 arguments. |
| `ffi.callback` | `ffi.callback(fn)` | `number` | Creates a native C function pointer trampoline that invokes a RayQuiro callback. |
| `ffi.close` | `ffi.close(lib)` | `void` | Unloads the dynamic library handle. |

---

## Usage Examples

### Calling Windows API Functions

```js
var k32 = ffi.load("kernel32.dll")
if (ffi.sym(k32, "GetCurrentProcessId")) {
    var pid = ffi.call(k32, "GetCurrentProcessId")
    print("Process ID: " + pid)
}
ffi.close(k32)
```

### Calling Standard C Library (libc / msvcrt)

```js
var lib = ffi.load("msvcrt.dll")
ffi.call(lib, "puts", "Hello from C puts!")
ffi.close(lib)
```

### Passing Buffers to Native Functions

When passing a `Buffer` object (created via `buffer.alloc` or `buffer.from_string`) as an argument to `ffi.call`, the raw memory pointer (`uint8_t*`) is automatically passed to the C function:

```js
var buf = buffer.from_string("Hello C library")
var lib = ffi.load("mylib.dll")
ffi.call(lib, "process_data", buf, buffer.size(buf))
ffi.close(lib)
```

### Passing Callbacks to C Code

Create native C function pointers from RayQuiro functions:

```js
var cb = ffi.callback(fn(a, b, c, d) {
    print("Callback called from C with sum: " + (a + b + c + d))
    return a + b
})

var lib = ffi.load("mylib.dll")
ffi.call(lib, "register_handler", cb)
ffi.close(lib)
```

