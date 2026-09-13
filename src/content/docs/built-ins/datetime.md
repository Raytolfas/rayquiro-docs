---
title: datetime
description: Current timestamp, date and time breakdown, calendar calculations, and formatting.
---

The `datetime` namespace provides functions to work with system time, timestamps, and date formatting.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `datetime.now` | `datetime.now()` | `object` | Returns current date/time component object. |
| `datetime.timestamp` | `datetime.timestamp()` | `number` | Returns Unix timestamp in seconds (floating point). |
| `datetime.format` | `datetime.format(ts, pattern)` | `string` | Formats a timestamp using pattern format specifiers. |

---

## Detailed Methods

### `datetime.now()`

Returns an object containing calendar and time components:

```js
var dt = datetime.now();
print("Year: " + str(dt["year"]));
print("Month: " + str(dt["month"]));
print("Day: " + str(dt["day"]));
print("Hour: " + str(dt["hour"]));
print("Minute: " + str(dt["minute"]));
print("Second: " + str(dt["second"]));
print("Millisecond: " + str(dt["ms"]));
print("Timestamp: " + str(dt["timestamp"]));
```

---

### `datetime.timestamp()`

Returns high-precision Unix timestamp in seconds (with fractional sub-second precision):

```js
var start = datetime.timestamp();

// Run heavy computation
var sum = 0;
var i = 0;
while (i < 100000) {
    sum = sum + i;
    i = i + 1;
}

var elapsed = datetime.timestamp() - start;
print("Computation took: " + str(elapsed) + " seconds");
```

---

### `datetime.format(timestamp, pattern)`

Formats a timestamp into a custom string representation:

| Specifier | Meaning | Example |
|-----------|---------|---------|
| `%Y` | 4-digit Year | `2026` |
| `%m` | 2-digit Month | `09` |
| `%d` | 2-digit Day | `12` |
| `%H` | 24-hour format | `14` |
| `%M` | Minute | `35` |
| `%S` | Second | `02` |

```js
var ts = datetime.timestamp();
var date_str = datetime.format(ts, "%Y-%m-%d %H:%M:%S");
print("Current time: " + date_str); // "2026-09-12 14:35:02"
```