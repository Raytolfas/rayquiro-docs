---
title: Types
description: Complete specification of RayQuiro primitive data types,
  collections, structs, and coercion rules.
slug: 0.2.1/language/types
---

RayQuiro is a dynamically typed language with first-class primitives, flexible collection types, and user-defined structures.

***

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

***

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

***

## 2. String

Strings are immutable sequences of UTF-8 characters enclosed in double quotes:

```js
var greeting = "Hello, RayQuiro!";
var length = len(greeting); // 16

// String Concatenation:
var full = "Count: " + str(42);
```

### Type Conversion

```js
var num_val = num("123.45"); // 123.45
var str_val = str(100);       // "100"
```

***

## 3. Boolean and Truthiness

Booleans can be either `true` or `false`:

```js
var is_active = true;
var is_admin = false;
```

### Truthiness Rules

When evaluated in conditionals (`if`, `while`):

* `false`, `null`, `0`, and `""` (empty string) evaluate to **falsy**.
* All other values evaluate to **truthy**.

***

## 4. Null

`null` represents the deliberate absence of any value:

```js
var user = null;

// Null coalescing:
var username = user ?? "Anonymous";
print(username); // "Anonymous"
```

***

## 5. Array

Arrays are ordered, dynamically sized lists of values:

```js
var inventory = ["potion", "shield", "sword"];

// Reading elements:
print(inventory[0]); // "potion"

// Modifying elements (Lvalue indexed assignment):
inventory[0] = "super_potion";

// Appending:
push(inventory, "helmet");

// Length:
print("Total items: " + str(len(inventory))); // 4
```

***

## 6. Object

Objects are key-value associative maps:

```js
var player = {
    name: "Aria",
    level: 25,
    health: 100.0
};

// Accessing fields:
print(player["name"]); // "Aria"

// Updating fields:
player["health"] = 85.0;

// Introspection:
var field_names = keys(player);   // ["name", "level", "health"]
var field_values = values(player); // ["Aria", 25, 85.0]
```

***

## 7. Structs

RayQuiro supports `struct` definitions for structured data models with default values:

```js
struct Item {
    id: 0,
    title: "Unknown Item",
    price: 0.0
}

var sword = Item { id: 101, title: "Iron Blade", price: 45.5 };
print(sword["title"]); // "Iron Blade"
print(sword["id"]);    // 101
```

***

## 8. Type Checking via `type(v)`

```js
print(type(42));           // "number"
print(type("text"));       // "string"
print(type(true));         // "bool"
print(type(null));         // "null"
print(type([1, 2]));       // "array"
print(type({ a: 1 }));     // "object"
print(type(fn() {}));      // "function"
```
