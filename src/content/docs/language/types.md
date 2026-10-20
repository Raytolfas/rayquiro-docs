---
title: Types
description: Complete specification of RayQuiro primitive data types, collections, structs, and coercion rules.
---

RayQuiro is a dynamically typed language with primitive types, collection types, and user-defined structures.

---

## Type System Overview

| Type | Type Identifier (`type()`) | Example Literals |
|------|----------------------------|------------------|
| **Number** | `"number"` | `42`, `3.14159`, `-0.5`, `1e6` |
| **String** | `"string"` | `"hello"`, `"UTF-8: Привет"`, `""` |
| **Boolean** | `"bool"` | `true`, `false` |
| **Null** | `"null"` | `null` |
| **Array** | `"array"` | `[]`, `[1, "two", 3.0]` |
| **Object** | `"object"` | `{}`, `{ name: "Hero", hp: 100 }` |
| **Function** | `"function"` | `fn(x) { return x; }` |

---

## 1. Number

All numbers in RayQuiro are IEEE 754 double-precision 64-bit floating point values (`double`).

```js
var integer_val = 100;
var float_val = 3.14159265;
var negative = -42;
```

### Built-in Math Functions

RayQuiro includes built-in math functions available globally:

| Function | Signature | Description |
|----------|-----------|-------------|
| `abs` | `abs(x)` | Absolute value. |
| `sqrt` | `sqrt(x)` | Square root. |
| `pow` | `pow(x, y)` | Raises `x` to power `y`. |
| `floor` | `floor(x)` | Rounds downward to the nearest integer. |
| `ceil` | `ceil(x)` | Rounds upward to the nearest integer. |
| `round` | `round(x)` | Rounds to the nearest integer. |
| `min` | `min(a, b)` | Returns the smaller of two numbers. |
| `max` | `max(a, b)` | Returns the larger of two numbers. |
| `clamp` | `clamp(x, min, max)` | Clamps `x` within `[min, max]`. |

---

## 2. String

Strings are immutable sequences of UTF-8 characters enclosed in double quotes:

```js
var greeting = "Hello, RayQuiro!";
var length = len(greeting);

var full = "Count: " + str(42);

var user = "Alice";
var score = 100;

var message1 = f"Player {user} has score {score + 10}!";
var message2 = `Welcome, ${user}!`;
```

### Type Conversion

```js
var num_val = num("123.45");
var str_val = str(100);
```

---

## 3. Boolean and Truthiness

Booleans can be either `true` or `false`:

```js
var is_active = true;
var is_admin = false;
```

### Truthiness Rules

When evaluated in conditionals (`if`, `while`):
- `false`, `null`, `0`, and `""` (empty string) evaluate to **falsy**.
- All other values evaluate to **truthy**.

---

## 4. Null

`null` represents the deliberate absence of any value:

```js
var user = null;

var username = user ?? "Anonymous";
print(username);
```

---

## 5. Array

Arrays are ordered, dynamically sized lists of values:

```js
var inventory = ["potion", "shield", "sword"];

print(inventory[0]);

inventory[0] = "super_potion";

push(inventory, "helmet");

print("Total items: " + str(len(inventory)));
```

---

## 6. Object

Objects are key-value associative maps:

```js
var player = {
    name: "Aria",
    level: 25,
    health: 100.0
};

print(player["name"]);

player["health"] = 85.0;

var field_names = keys(player);
var field_values = values(player);
```

---

## 7. Structs

RayQuiro supports `struct` definitions for structured data models with default values:

```js
struct Item {
    id: 0,
    title: "Unknown Item",
    price: 0.0
}

var sword = Item { id: 101, title: "Iron Blade", price: 45.5 };
print(sword["title"]);
print(sword["id"]);
```

---

## 8. Type Checking via `type(v)`

```js
print(type(42));
print(type("text"));
print(type(true));
print(type(null));
print(type([1, 2]));
print(type({ a: 1 }));
print(type(fn() {}));
```
