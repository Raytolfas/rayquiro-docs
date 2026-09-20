---
title: Standard Library & Global Built-ins
description: Complete reference of all global functions, math built-ins, and data manipulation utilities available without imports in RayQuiro.
---

RayQuiro includes a comprehensive suite of built-in functions that are globally accessible from any script without needing an `import` statement.

---

## 1. Core & I/O

| Function | Signature | Description |
|----------|-----------|-------------|
| `print` | `print(...args)` | Prints arguments separated by space to stdout, followed by a newline. |
| `assert` | `assert(condition, message = "")` | Throws a runtime error if `condition` is falsy. |
| `type` | `type(value)` | Returns the type name: `"number"`, `"string"`, `"bool"`, `"array"`, `"object"`, `"function"`, or `"null"`. |

```js
print("Hello", 42, true); // Hello 42 true
assert(2 + 2 == 4, "Math error!");
print(type("text")); // "string"
print(type([1, 2])); // "array"
```

---

## 2. Type Conversion

| Function | Signature | Description |
|----------|-----------|-------------|
| `str` | `str(value)` | Converts any value to its string representation (alias: `to_string`). |
| `to_string` | `to_string(value)` | Equivalent to `str(value)`. |
| `num` | `num(value)` | Parses a string or boolean into a floating-point number. |
| `bool` | `bool(value)` | Converts a value into a boolean based on truthiness. |

```js
var n = num("3.1415");
var s = str(100);
var b = bool(1); // true
```

---

## 3. Sequences, Arrays & Objects

| Function | Signature | Description |
|----------|-----------|-------------|
| `len` | `len(container)` | Returns the number of characters in a string, elements in an array, or keys in an object. |
| `length` | `length(container)` | Alias for `len(container)`. |
| `range` | `range(stop)` / `range(start, stop, step = 1)` | Generates an array of numbers from `start` to `stop` (exclusive). |
| `push` | `push(array, value)` | Appends `value` to the end of `array`. |
| `pop` | `pop(array)` | Removes and returns the last element of `array`. |
| `join` | `join(array, separator = "")` | Concatenates elements of `array` into a string separated by `separator`. |
| `split` | `split(str, separator = "")` | Splits `str` by `separator` into an array of substrings. |
| `keys` | `keys(object)` | Returns an array of keys belonging to `object`. |
| `values` | `values(object)` | Returns an array of values belonging to `object`. |
| `map` | `map(array, fn)` | Transforms each element in `array` using `fn(item)`. |
| `filter` | `filter(array, fn)` | Returns elements in `array` that satisfy predicate `fn(item)`. |
| `reduce` | `reduce(array, fn, initial)` | Reduces `array` to a single value using accumulator `fn(acc, item)`. |

```js
var nums = range(1, 5); // [1, 2, 3, 4]
push(nums, 5);          // [1, 2, 3, 4, 5]
var last = pop(nums);   // 5

var doubled = map(nums, fn(x) { return x * 2; });
var evens = filter(nums, fn(x) { return x % 2 == 0; });
var sum = reduce(nums, fn(acc, x) { return acc + x; }, 0);

var words = split("rayquiro is fast", " ");
var sentence = join(words, "-"); // "rayquiro-is-fast"
```

---

## 4. Mathematical Functions

RayQuiro includes high-precision mathematical operations accessible directly:

| Function | Signature | Description |
|----------|-----------|-------------|
| `sqrt` | `sqrt(x)` | Returns the square root of `x`. |
| `abs` | `abs(x)` | Returns the absolute value of `x`. |
| `pow` | `pow(x, y)` | Returns `x` raised to the power of `y`. |
| `sin` | `sin(rad)` | Sine of angle in radians. |
| `cos` | `cos(rad)` | Cosine of angle in radians. |
| `tan` | `tan(rad)` | Tangent of angle in radians. |
| `log` | `log(x)` | Natural logarithm (base $e$) of `x`. |
| `floor` | `floor(x)` | Largest integer less than or equal to `x`. |
| `ceil` | `ceil(x)` | Smallest integer greater than or equal to `x`. |
| `round` | `round(x)` | Rounds `x` to the nearest integer. |
| `min` | `min(a, b)` | Returns the lesser of `a` and `b`. |
| `max` | `max(a, b)` | Returns the greater of `a` and `b`. |
| `clamp` | `clamp(x, min, max)` | Constrains `x` within `[min, max]`. |
| `pi` | `pi` | Mathematical constant $\pi$ ($3.141592653589793$). |

```js
print(sqrt(16));       // 4
print(pow(2, 8));      // 256
print(clamp(15, 0, 10)); // 10
print(cos(pi));        // -1
```

---

## 5. Execution & Sleep

| Function | Signature | Description |
|----------|-----------|-------------|
| `sleep` | `sleep(ms)` | Blocks the current thread for the specified number of milliseconds (also available as `time.sleep`). |

```js
print("Waiting 500ms...");
sleep(500);
print("Done!");
```
