---
title: Test Runner
description: Automated test execution and assertions in RayQuiro
---

# `rqio test`

RayQuiro 0.2.2 comes with a built-in automated test runner.

## Usage

```bash
# Run all tests in the project (searches tests/ or *_test.rq files)
rqio test

# Run tests in a specific directory or file
rqio test tests/01_basic_syntax.rq
rqio test tests/
```

## Writing Tests

You can write tests with assertions directly in your script:

```rq
var name = "RayQuiro";
var ver = 2;

// String interpolation
var banner = f"{name} v0.{ver}";
assert_eq(banner, "RayQuiro v0.2");

// Pattern matching
var status = 200;
var statusText = "";
match status {
    200 => statusText = "OK",
    404 => statusText = "Not Found",
    _ => statusText = "Unknown"
}
assert_eq(statusText, "OK");

// General assertions
assert(10 > 5, "Math check failed");
assert_true(true);
assert_false(false);
assert_null(null);
assert_ne(1, 2);
```

## Assertion Functions

| Function | Description |
|---|---|
| `assert(condition, message)` | Asserts that `condition` is truthy |
| `assert_eq(actual, expected, message)` | Asserts that `actual == expected` |
| `assert_ne(actual, expected, message)` | Asserts that `actual != expected` |
| `assert_true(value, message)` | Asserts that `value` is `true` |
| `assert_false(value, message)` | Asserts that `value` is `false` |
| `assert_null(value, message)` | Asserts that `value` is `null` |
