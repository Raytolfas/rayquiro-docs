---
title: regex
description: Regular expression matching, testing, replacement, and splitting.
slug: 0.2.1/built-ins/regex
---

The `regex` namespace provides full ECMAScript-compatible regular expression capabilities.

## regex.test

Check if a string matches a pattern.

```js
regex.test(str, pattern) -> bool
```

```js
var valid = regex.test("hello@example.com", "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$");
print(valid); // true
```

***

## regex.match

Find all matches of a pattern in a string.

```js
regex.match(str, pattern) -> array
```

```js
var numbers = regex.match("Order #42 cost $99 with item #105", "\\d+");
print(numbers); // ["42", "99", "105"]
```

***

## regex.replace

Replace occurrences matching a pattern.

```js
regex.replace(str, pattern, replacement) -> string
```

```js
var sanitized = regex.replace("user_123_temp", "_temp$", "");
print(sanitized); // user_123
```

***

## regex.split

Split a string by a regular expression delimiter.

```js
regex.split(str, pattern) -> array
```

```js
var parts = regex.split("apple, banana; orange : grape", "[,;: ]+");
print(parts); // ["apple", "banana", "orange", "grape"]
```
