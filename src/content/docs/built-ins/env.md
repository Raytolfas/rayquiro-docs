---
title: env
description: Reading, setting, and inspecting operating system environment variables.
---

The `env` namespace provides straightforward access to process environment variables. No import is required.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `env.get` | `env.get(key, default = null)` | `string \| null` | Retrieves value of an environment variable. |
| `env.set` | `env.set(key, val)` | `bool` | Sets or updates an environment variable. |
| `env.has` | `env.has(key)` | `bool` | Checks if an environment variable is defined. |
| `env.all` | `env.all()` | `object` | Returns all environment variables as a key-value map. |
| `env.path_add` | `env.path_add(dir)` | `bool` | Prepends or appends a directory to system `PATH`. |

---

## Detailed Methods

### `env.get(key, default = null)`

Retrieves the value of environment variable `key`:

```js
var port = env.get("PORT", "8080");
var secret = env.get("API_SECRET");

if (secret == null) {
    print("Warning: API_SECRET not set!");
}
```

---

### `env.set(key, val)`

Sets an environment variable for the current process:

```js
env.set("APP_ENV", "production");
print("Mode: " + env.get("APP_ENV"));
```

---

### `env.has(key)`

```js
if (env.has("DEBUG")) {
    print("Debug mode enabled.");
}
```

---

### `env.path_add(directory)`

Adds a new directory to the system executable search `PATH`:

```js
env.path_add("C:/rayquiro/bin");
```