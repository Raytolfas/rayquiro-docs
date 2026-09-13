---
title: env
description: Reading, setting, and inspecting operating system environment variables.
---

The `env` namespace provides straightforward access to process environment variables.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `env.get` | `env.get(key, default)` | `string \| null` | Retrieves value of an environment variable. |
| `env.set` | `env.set(key, val)` | `void` | Sets or updates an environment variable. |
| `env.has` | `env.has(key)` | `bool` | Checks if an environment variable is defined. |
| `env.all` | `env.all()` | `object` | Returns all environment variables as a key-value map. |

---

## Detailed Methods

### `env.get(key, default_val = null)`

Retrieves the value of environment variable `key`. If the variable is not set, returns `default_val` (or `null` if not specified):

```js
var port = env.get("PORT", "8080");
var api_key = env.get("API_SECRET");

if (api_key == null) {
    print("Warning: API_SECRET is not configured!");
}
```

---

### `env.set(key, val)`

Sets an environment variable for the current process and its spawned children:

```js
env.set("APP_ENV", "production");
print("Mode: " + env.get("APP_ENV")); // "production"
```

---

### `env.has(key)`

Returns `true` if the environment variable exists, otherwise `false`:

```js
if (env.has("CI")) {
    print("Running inside Continuous Integration environment.");
}
```

---

### `env.all()`

Dumps all current environment variables into a RayQuiro object:

```js
var vars = env.all();
print("Home Directory: " + vars["HOME"]);
print("Current Path: " + vars["PATH"]);
```