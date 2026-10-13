---
title: time
description: Delays, pauses, timers, monotonic clock, and performance benchmarking.
---

The `time` namespace provides timing primitives and thread sleeping. No import is required.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `time.sleep` | `time.sleep(ms)` | `void` | Pauses execution for the specified milliseconds (alias: `sleep(ms)`). |
| `time.now_ms` | `time.now_ms()` | `number` | Returns high-precision monotonic clock in milliseconds (alias: `clock.ms()`). |
| `time.unix_ms` | `time.unix_ms()` | `number` | Returns current Unix epoch time in milliseconds. |

---

## Detailed Methods

### `time.sleep(ms)`

Suspends the running process or thread for `ms` milliseconds.

```js
print("Starting countdown...");
var i = 3;
while (i > 0) {
    print(str(i) + "...");
    time.sleep(1000);
    i = i - 1;
}
print("Launch!");
```

---

### `time.now_ms()`

Returns the high-resolution monotonic time in milliseconds since system boot. Unaffected by system clock changes or daylight saving adjustments:

```js
var start_ms = time.now_ms();

var i = 0;
while (i < 500000) { i = i + 1; }

var duration = time.now_ms() - start_ms;
print("Execution time: " + str(duration) + " ms");
```