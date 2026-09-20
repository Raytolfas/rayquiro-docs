---
title: crypto
description: Cryptographic hashing, secure random bytes, UUIDs, Base64 encoding,
  and HMAC signatures.
slug: 0.2.1/built-ins/crypto
---

The `crypto` namespace provides essential cryptography and encoding primitives without needing any external C or Python dependencies.

***

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `crypto.uuid` | `crypto.uuid()` | `string` | Generates a random RFC 4122 v4 UUID string. |
| `crypto.random_bytes` | `crypto.random_bytes(n)` | `string` | Generates `n` cryptographically secure random bytes (hex). |
| `crypto.sha256` | `crypto.sha256(str)` | `string` | Computes SHA-256 hexadecimal digest. |
| `crypto.sha1` | `crypto.sha1(str)` | `string` | Computes SHA-1 hexadecimal digest. |
| `crypto.md5` | `crypto.md5(str)` | `string` | Computes MD5 hexadecimal digest. |
| `crypto.hmac_sha256` | `crypto.hmac_sha256(msg, key)` | `string` | Generates an HMAC-SHA256 signature. |
| `crypto.base64_encode` | `crypto.base64_encode(str)` | `string` | Encodes string into Base64 format. |
| `crypto.base64_decode` | `crypto.base64_decode(b64)` | `string` | Decodes a Base64 string. |

***

## Detailed Methods

### `crypto.uuid()`

Generates a cryptographically strong UUID version 4:

```js
var id = crypto.uuid();
print("Session ID: " + id);
// Example: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
```

***

### `crypto.sha256(input)`

Calculates standard 256-bit SHA-2 digest:

```js
var hash = crypto.sha256("password123");
print("Hash: " + hash);
// "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
```

***

### `crypto.hmac_sha256(message, secret_key)`

Produces an HMAC authentication signature using SHA-256:

```js
var payload = "GET /api/v1/orders";
var secret = "my_super_secret_key";

var signature = crypto.hmac_sha256(payload, secret);
print("API Signature: " + signature);
```

***

### `crypto.base64_encode(text)` & `crypto.base64_decode(encoded)`

Fast binary-to-text Base64 conversions:

```js
var raw = "Hello, RayQuiro!";
var encoded = crypto.base64_encode(raw);
print("Base64: " + encoded); // "SGVsbG8sIFJheVF1aXJvIQ=="

var decoded = crypto.base64_decode(encoded);
print("Restored: " + decoded); // "Hello, RayQuiro!"
```

***

### `crypto.random_bytes(count)`

Generates random cryptographically secure hex strings:

```js
var token = crypto.random_bytes(16);
print("Csrf Token: " + token);
```
