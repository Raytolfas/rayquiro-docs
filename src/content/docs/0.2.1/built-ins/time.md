---
title: time
description: Delays, pauses, timers, and performance benchmarking.
slug: 0.2.1/built-ins/time
---

The `time` namespace provides timing primitives and thread sleeping.

***

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `time.sleep` | `time.sleep(ms)` | `void` | Pauses execution for the specified milliseconds. |
| `time.ms` | `time.ms()` | `number` | Returns monotonic system milliseconds counter. |

***

## Detailed Methods

### `time.sleep(ms)`

Suspends the running process or thread for `ms` milliseconds.

```js
print("Starting countdown...");
var i = 3;
while (i > 0) {
    print(str(i) + "...");
    time.sleep(1000); // 1 second
    i = i - 1;
}
print("Liftoff!");
```

***

### `time.ms()`

Returns the high-resolution monotonic time in milliseconds since system boot. Unaffected by system clock changes or daylight saving adjustments, making it ideal for games, animations, and benchmarking:

```js
var start_ms = time.ms();

// Perform operations
var i = 0;
while (i < 500000) { i = i + 1; }

var duration = time.ms() - start_ms;
print("Execution time: " + str(duration) + " ms");
```
