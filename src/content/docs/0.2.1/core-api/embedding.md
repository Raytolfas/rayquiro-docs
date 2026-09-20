---
title: Embedding Examples
description: Complete step-by-step examples for embedding rqio_core into C++,
  C#, and Python.
slug: 0.2.1/core-api/embedding
---

This guide shows how to integrate `rqio_core.dll` (Windows) or `rqio_core.so` (Linux) into external host applications.

***

## 1. C++ Example

### Direct C ABI Integration

```cpp
#include <iostream>
#include "rayquiro/RqioCoreAPI.h"

int main() {
    std::cout << "Using RayQuiro Core v" << rqio_core_version() << std::endl;

    RqioCoreHandle* runtime = nullptr;
    char* error = nullptr;

    if (rqio_core_create(".", "", &runtime, &error) != RQIO_CORE_OK) {
        std::cerr << "Failed to create runtime: " << error << std::endl;
        rqio_core_free_string(error);
        return 1;
    }

    const char* script = 
        "var x = random.int(10, 50);\n"
        "print(\"RayQuiro computed:\", x * 2);\n";

    int exitCode = 0;
    if (rqio_core_run_source(runtime, "embedded.rq", script, 0, &exitCode, &error) != RQIO_CORE_OK) {
        std::cerr << "Execution error: " << error << std::endl;
        rqio_core_free_string(error);
    } else {
        std::cout << "Script exited with code: " << exitCode << std::endl;
    }

    rqio_core_destroy(runtime);
    return 0;
}
```

### Linking with GCC / Clang

```bash
# Windows
g++ main.cpp -Iinclude -L. -lrqio_core -o host.exe

# Linux
clang++ main.cpp -Iinclude -L. -lrqio_core -Wl,-rpath,. -o host
```

***

## 2. C# (.NET) Example

Using P/Invoke to run RayQuiro scripts inside Unity, Godot, or any .NET 8 / C# application:

```csharp
using System;
using System.Runtime.InteropServices;

public static class RayQuiro
{
    private const string DllName = "rqio_core";

    [DllImport(DllName, CallingConvention = CallingConvention.Cdecl)]
    public static extern IntPtr rqio_core_version();

    [DllImport(DllName, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rqio_core_create(
        string projectRoot,
        string executablePath,
        out IntPtr outHandle,
        out IntPtr outError);

    [DllImport(DllName, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rqio_core_destroy(IntPtr handle);

    [DllImport(DllName, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rqio_core_run_source(
        IntPtr handle,
        string virtualFilename,
        string sourceCode,
        int preferVm,
        out int outExitCode,
        out IntPtr outError);

    [DllImport(DllName, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rqio_core_free_string(IntPtr value);

    public static string GetVersion()
    {
        return Marshal.PtrToStringAnsi(rqio_core_version()) ?? "unknown";
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine($"RayQuiro Core: {RayQuiro.GetVersion()}");

        if (RayQuiro.rqio_core_create(".", "", out IntPtr handle, out IntPtr errPtr) != 0)
        {
            string err = Marshal.PtrToStringAnsi(errPtr);
            RayQuiro.rqio_core_free_string(errPtr);
            Console.WriteLine($"Init error: {err}");
            return;
        }

        string code = "print('Hello from RayQuiro in C#! Random number:', random.int(100, 999));";

        if (RayQuiro.rqio_core_run_source(handle, "csharp_script.rq", code, 0, out int exitCode, out IntPtr runErr) != 0)
        {
            string err = Marshal.PtrToStringAnsi(runErr);
            RayQuiro.rqio_core_free_string(runErr);
            Console.WriteLine($"Run error: {err}");
        }

        RayQuiro.rqio_core_destroy(handle);
    }
}
```

***

## 3. Python Example (`ctypes`)

```python
import ctypes
import os
import sys

# Load shared library
lib_name = "rqio_core.dll" if sys.platform == "win32" else "rqio_core.so"
rqio = ctypes.CDLL(os.path.abspath(lib_name))

# Configure argument and return types
rqio.rqio_core_version.restype = ctypes.c_char_p

rqio.rqio_core_create.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char_p)]
rqio.rqio_core_create.restype = ctypes.c_int

rqio.rqio_core_destroy.argtypes = [ctypes.c_void_p]

rqio.rqio_core_run_source.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_char_p)
]
rqio.rqio_core_run_source.restype = ctypes.c_int

rqio.rqio_core_free_string.argtypes = [ctypes.c_char_p]

# Execute
print("RayQuiro Version:", rqio.rqio_core_version().decode("utf-8"))

handle = ctypes.c_void_p()
err = ctypes.c_char_p()

if rqio.rqio_core_create(b".", b"", ctypes.byref(handle), ctypes.byref(err)) != 0:
    print("Failed to initialize:", err.value.decode("utf-8"))
    rqio.rqio_core_free_string(err)
    sys.exit(1)

script = b"""
var list = [10, 20, 30, 40, 50];
random.shuffle(list);
print("Shuffled in Python:", list);
"""

exit_code = ctypes.c_int(0)
res = rqio.rqio_core_run_source(handle, b"embedded.rq", script, 0, ctypes.byref(exit_code), ctypes.byref(err))

if res != 0:
    print("Error:", err.value.decode("utf-8"))
    rqio.rqio_core_free_string(err)

rqio.rqio_core_destroy(handle)
```
