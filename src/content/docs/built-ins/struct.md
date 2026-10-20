---
title: struct
description: C-ABI binary data packing, memory alignment, and byte layout serialization.
---

The `struct` module provides binary data serialization and memory alignment utilities, allowing RayQuiro to pack variables into contiguous binary byte buffers and unpack binary data received from C libraries, network sockets, or binary file formats.

---

## Format Specifiers

| Specifier | C Type | Size (Bytes) | Range |
|-----------|--------|--------------|-------|
| `b` | `int8_t` | 1 | -128 .. 127 |
| `B` | `uint8_t` | 1 | 0 .. 255 |
| `h` | `int16_t` | 2 | -32,768 .. 32,767 |
| `H` | `uint16_t` | 2 | 0 .. 65,535 |
| `i`, `l` | `int32_t` | 4 | -2,147,483,648 .. 2,147,483,647 |
| `I`, `L` | `uint32_t` | 4 | 0 .. 4,294,967,295 |
| `q` | `int64_t` | 8 | -9,223,372,036,854,775,808 .. 9,223,372,036,854,775,807 |
| `Q` | `uint64_t` | 8 | 0 .. 18,446,744,073,709,551,615 |
| `f` | `float` | 4 | IEEE-754 32-bit single precision |
| `d` | `double` | 8 | IEEE-754 64-bit double precision |
| `p` | `intptr_t` | 8 | Pointer / buffer address |

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `struct.calcsize` | `struct.calcsize(format)` | `number` | Calculates total byte size required by the format string. |
| `struct.pack` | `struct.pack(format, ...values)` | `Buffer` | Packs arguments into a contiguous binary byte buffer. |
| `struct.unpack` | `struct.unpack(format, buffer, [offset])` | `array` | Unpacks values from a buffer according to the format string. |

---

## Usage Examples

### Packing and Unpacking Binary Packets

```js
var size = struct.calcsize("b h i d")
print("Struct size: " + size)

var buf = struct.pack("b h i d", 1, 500, 100000, 3.14159)
var values = struct.unpack("b h i d", buf, 0)

print(values[0])
print(values[1])
print(values[2])
print(values[3])
```

### Passing Packed Structs to C FFI

```js
var rect = struct.pack("i i i i", 10, 20, 800, 600)
var lib = ffi.load("user32.dll")
ffi.close(lib)
```
