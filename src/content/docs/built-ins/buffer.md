---
title: buffer
description: Raw binary memory buffers for network protocols, binary formats, and C FFI data exchange.
---

The `buffer` module provides low-level contiguous byte arrays with read and write operations for unsigned 8-bit integers, 32-bit signed integers, and 64-bit IEEE-754 floating point numbers.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `buffer.alloc` | `buffer.alloc(size)` | `Buffer` | Allocates a zeroed byte buffer of the specified size in bytes. |
| `buffer.from_string` | `buffer.from_string(str)` | `Buffer` | Creates a buffer initialized with the UTF-8 bytes of a string. |
| `buffer.to_string` | `buffer.to_string(buf)` | `string` | Converts buffer bytes into a string. |
| `buffer.size` | `buffer.size(buf)` | `number` | Returns total buffer size in bytes (alias: `buffer.len`). |
| `buffer.get_u8` | `buffer.get_u8(buf, offset)` | `number` | Reads a single unsigned 8-bit integer (0-255). |
| `buffer.set_u8` | `buffer.set_u8(buf, offset, val)` | `void` | Writes a single unsigned 8-bit integer (0-255). |
| `buffer.get_i32` | `buffer.get_i32(buf, offset)` | `number` | Reads a 32-bit signed integer (little-endian). |
| `buffer.set_i32` | `buffer.set_i32(buf, offset, val)` | `void` | Writes a 32-bit signed integer (little-endian). |
| `buffer.get_f64` | `buffer.get_f64(buf, offset)` | `number` | Reads a 64-bit double precision float. |
| `buffer.set_f64` | `buffer.set_f64(buf, offset, val)` | `void` | Writes a 64-bit double precision float. |

---

## Usage Examples

### Allocating and Mutating Bytes

```js
var buf = buffer.alloc(32)
buffer.set_u8(buf, 0, 0x52)
buffer.set_u8(buf, 1, 0x51)

var b0 = buffer.get_u8(buf, 0)
var b1 = buffer.get_u8(buf, 1)
print(b0)
print(b1)
```

### Storing Binary Numbers

```js
var packet = buffer.alloc(16)
buffer.set_i32(packet, 0, 1001)
buffer.set_f64(packet, 4, 3.14159265)

var packetId = buffer.get_i32(packet, 0)
var val = buffer.get_f64(packet, 4)
print("Packet ID: " + packetId)
print("Value: " + val)
```

### Converting Strings and Interfacing with FFI

```js
var textBuf = buffer.from_string("Hello World")
var str = buffer.to_string(textBuf)
print(str)

var lib = ffi.load("kernel32.dll")
ffi.close(lib)
```
