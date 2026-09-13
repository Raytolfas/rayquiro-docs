---
title: Operators
description: Complete operators reference for RayQuiro.
---

RayQuiro features a full set of operators for arithmetic, logic, null-safety, and assignment.

---

## 1. Arithmetic Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Addition / String Concat | `10 + 5`, `"a" + "b"` | `15`, `"ab"` |
| `-` | Subtraction / Negation | `10 - 4`, `-x` | `6` |
| `*` | Multiplication | `6 * 7` | `42` |
| `/` | Division (floating point) | `10 / 4` | `2.5` |
| `%` | Modulo (remainder) | `10 % 3` | `1` |

---

## 2. Comparison Operators

Comparisons evaluate to boolean `true` or `false`:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equality | `x == 10` |
| `!=` | Inequality | `x != 0` |
| `<` | Less than | `score < 50` |
| `<=` | Less than or equal | `count <= 10` |
| `>` | Greater than | `health > 0` |
| `>=` | Greater than or equal | `level >= 18` |

---

## 3. Logical Operators

| Operator | Name | Behavior |
|----------|------|----------|
| `&&` | Logical AND | Returns truthy if both operands are truthy. Short-circuits. |
| `\|\|` | Logical OR | Returns truthy if either operand is truthy. Short-circuits. |
| `!` | Logical NOT | Inverts truthiness (`!true` is `false`, `!0` is `true`). |

```js
if (user != null && user["is_admin"] && user["level"] >= 10) {
    grant_access();
}
```

---

## 4. Null-Safety Operators

### Null Coalescing (`??`)

Returns the right-hand operand when the left-hand operand is `null`:

```js
var username = input_name ?? "Guest";
```

### Optional Chaining (`?.`)

Safely accesses nested properties or indices without crashing if intermediate values are `null`:

```js
var server_host = config?.["network"]?.["host"] ?? "127.0.0.1";
```

---

## 5. Assignment Operators

| Operator | Meaning | Equivalent |
|----------|---------|------------|
| `=` | Simple assignment | `x = 5` |
| `+=` | Add and assign | `x = x + 2` |
| `-=` | Subtract and assign | `x = x - 2` |
| `*=` | Multiply and assign | `x = x * 2` |
| `/=` | Divide and assign | `x = x / 2` |

RayQuiro also supports **lvalue indexed assignment** on collections:

```js
inventory[0] = "Shield";
player["health"] = 100;
```