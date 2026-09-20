---
title: json
description: JSON parsing, serializing, formatting, and object conversion in RayQuiro.
slug: 0.2.1/built-ins/json
---

The `json` namespace provides high-performance JSON encoding and decoding. Built into RayQuiro's runtime without requiring any imports.

***

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `json.parse` | `json.parse(str)` | `object \| array \| value` | Parses a JSON string into RayQuiro values. |
| `json.stringify` | `json.stringify(val)` | `string` | Converts a RayQuiro value to a compact JSON string. |
| `json.pretty` | `json.pretty(val, indent)` | `string` | Converts a RayQuiro value to formatted, indented JSON. |

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
// Output: {"badges":["pioneer","tester"],"level":15,"username":"alex","verified":true}
```

***

### `json.pretty(val, indent = 2)`

Serializes data into an indented, human-readable JSON string suitable for configuration files and debugging.

```js
var settings = {
    graphics: {
        width: 1920,
        height: 1080,
        vsync: true
    },
    audio: {
        volume: 0.8
    }
};

var formatted = json.pretty(settings, 2);
fs.write("settings.json", formatted);
```

***

## Type Conversion Table

| JSON Type | RayQuiro Equivalent |
|-----------|---------------------|
| `object` (`{}`) | Object / Key-Value Map |
| `array` (`[]`) | Array (`[]`) |
| `string` (`"..."`) | String (`"..."`) |
| `number` (`42`, `3.14`) | Number (64-bit IEEE double) |
| `boolean` (`true` / `false`) | Boolean (`true` / `false`) |
| `null` | `null` |
