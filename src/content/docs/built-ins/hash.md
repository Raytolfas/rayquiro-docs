---
title: hash
description: Fast cryptographic and non-cryptographic hashing shortcuts.
---

The `hash` namespace provides direct access to common hashing algorithms.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `hash.sha256` | `hash.sha256(str)` | `string` | Computes SHA-256 digest in lowercase hexadecimal. |
| `hash.sha1` | `hash.sha1(str)` | `string` | Computes SHA-1 digest in lowercase hexadecimal. |

---

## Examples

```js
var file_content = fs.read("package.json");
var checksum = hash.sha256(file_content);

print("SHA-256 Checksum: " + checksum);
```