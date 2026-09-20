---
title: random
description: Built-in package for pseudo-random number generation, sampling, and shuffling.
slug: 0.2.1/built-ins/random
---

The `random` package provides high-performance pseudo-random number generation functions. It is available globally out-of-the-box without requiring any `import` statement.

## API Reference

### `random.int(min, max)`

Returns a pseudo-random integer in the range `[min, max]` (inclusive of both boundaries).

* **Parameters:**
  * `min` (number): Lower integer boundary.
  * `max` (number): Upper integer boundary.
* **Returns:** (number) An integer between `min` and `max`.

```rq
var roll = random.int(1, 6)
print("Dice roll: " + roll)

var enemyHp = random.int(50, 100)
```

### `random.float()`

Returns a pseudo-random floating-point number in the range `[0.0, 1.0)`.

* **Returns:** (number) Floating-point number in `[0.0, 1.0)`.

```rq
var chance = random.float()
if (chance < 0.25) {
    print("Critical strike!")
}
```

### `random.choice(array)`

Selects and returns a random element from the provided array.

* **Parameters:**
  * `array` (array): Non-empty array of values.
* **Returns:** (any) A randomly selected item from the array, or `null` if the array is empty.

```rq
var colors = ["red", "green", "blue", "yellow", "purple"]
var picked = random.choice(colors)
print("Chosen color: " + picked)
```

### `random.shuffle(array)`

Randomly shuffles the elements of an array in place using the Fisher-Yates algorithm and returns the array.

* **Parameters:**
  * `array` (array): Array to shuffle.
* **Returns:** (array) The shuffled array.

```rq
var deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(deck)
print("Shuffled deck: " + deck)
```

### Global `rand(min, max)`

For convenience, `rand(min, max)` is also available as a global function alias to `random.int(min, max)`.

```rq
var coin = rand(0, 1)
print(coin == 1 ? "Heads" : "Tails")
```
