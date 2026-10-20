---
title: json
description: JSON parsing, serializing, and object conversion in RayQuiro.
slug: 1.0/built-ins/json
---

The `json` namespace provides high-performance JSON encoding and decoding. Built into RayQuiro's runtime without requiring any imports.

***

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `json.parse` | `json.parse(str)` | `object \| array \| value` | Parses a JSON string into RayQuiro values. |
| `json.stringify` | `json.stringify(val)` | `string` | Converts a RayQuiro value to a JSON string. |

***

## Detailed Methods

### `json.parse(str)`

Parses a JSON string into RayQuiro native primitives (objects, arrays, strings, numbers, booleans, or null). Throws an error on malformed syntax.

```js
var json_str = "{\"id\": 42, \"name\": \"Player1\", \"inventory\": [\"sword\", \"shield\"]}";

try {
    var data = json.parse(json_str);
    print("Player ID: " + str(data["id"]));
    print("First Item: " + data["inventory"][0]);
} catch (err) {
    print("Invalid JSON: " + err);
}
```

***

### `json.stringify(val)`

Serializes a RayQuiro value (table, array, string, number, bool, null) into a standard JSON string.

```js
var user = {
    username: "alex",
    level: 15,
    verified: true,
    badges: ["pioneer", "tester"]
};

var compact_json = json.stringify(user);
print(compact_json);
```
