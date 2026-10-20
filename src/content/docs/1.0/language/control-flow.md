---
title: Control Flow
description: Conditionals, while loops, for-in iteration, break, and continue in RayQuiro.
slug: 1.0/language/control-flow
---

RayQuiro provides standard control flow statements for branching and looping.

***

## 1. Conditionals (`if / else if / else`)

```js
var score = 85;

if (score >= 90) {
    print("Grade: A");
} else if (score >= 80) {
    print("Grade: B");
} else if (score >= 70) {
    print("Grade: C");
} else {
    print("Grade: F");
}
```

Parentheses around the condition are optional or standard, braces `{}` around the block are required.

***

## 2. While Loops

The `while` loop executes its body repeatedly as long as its condition evaluates to a truthy value:

```js
var count = 0;

while (count < 5) {
    print("Iteration: " + str(count));
    count = count + 1;
}
```

***

## 3. Loop Control (`break` and `continue`)

### `break`

Terminates the innermost loop immediately:

```js
var i = 0;
while (i < 100) {
    if (i == 42) {
        print("Found target: 42. Halting loop.");
        break;
    }
    i = i + 1;
}
```

### `continue`

Skips the remainder of the current iteration and jumps to the next condition evaluation:

```js
var n = 0;
while (n < 10) {
    n = n + 1;
    if (n % 2 == 0) {
        continue;
    }
    print("Odd number: " + str(n));
}
```

***

## 4. Array Iteration Pattern

````js
var fruits = ["apple", "banana", "cherry", "date"];
var idx = 0;

while (idx < len(fruits)) {
    var item = fruits[idx];
    print("Fruit #" + str(idx + 1) + ": " + item);
    idx = idx + 1;
}

---

## 5. Pattern Matching (`match`)

RayQuiro includes pattern matching without fallthrough:

```js
var status = 200;

match status {
    200 => print("OK"),
    400 => print("Bad Request"),
    404 => print("Not Found"),
    500 => {
        print("Internal Server Error");
        log_error("Server down");
    },
    _ => print("Unknown Status Code")
}
````

* Each pattern is evaluated in order; the first match executes and terminates the `match` construct immediately (no `break` needed).
* Use `_` (wildcard) or `default` to handle fallback cases.
* Both single statement expressions and `{ ... }` code blocks are supported on the right side of `=>`.

```
```
