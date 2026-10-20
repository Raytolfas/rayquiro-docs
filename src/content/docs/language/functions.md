---
title: Functions
description: Reference for function definitions, parameters, closures, multiple returns, and recursion in RayQuiro.
---

Functions are first-class citizens in RayQuiro. They can be stored in variables, passed into other functions as arguments, returned from functions, and executed synchronously or asynchronously.

---

## 1. Defining Functions

Functions are declared with the `fn` keyword followed by a name, parameter list in parentheses, and a code block in braces:

```js
fn add(a, b) {
    return a + b;
}

var sum = add(10, 25);
print("Sum: " + str(sum));
```

If a function completes execution without a `return` statement, it returns `null` implicitly.

---

## 2. Default Parameter Values

You can specify default values for parameters. If the caller omits that argument, the default expression is evaluated:

```js
fn greet(name = "World", prefix = "Hello") {
    return prefix + ", " + name + "!";
}

print(greet());
print(greet("Alice"));
print(greet("Bob", "Good day"));
```

---

## 3. Variadic Arguments (`...rest`)

Functions can accept any number of variable arguments by prefixing the final parameter with `...`:

```js
fn sum_all(...numbers) {
    var total = 0;
    var i = 0;
    while (i < len(numbers)) {
        total = total + numbers[i];
        i = i + 1;
    }
    return total;
}

print(sum_all(1, 2, 3, 4, 5));
print(sum_all(10, 20));
```

---

## 4. Multiple Return Values

RayQuiro supports returning multiple values separated by commas:

```js
fn divmod(dividend, divisor) {
    var quotient = floor(dividend / divisor);
    var remainder = dividend % divisor;
    return quotient, remainder;
}

var [q, r] = divmod(10, 3);
print("Quotient: " + str(q));
print("Remainder: " + str(r));
```

---

## 5. Anonymous Functions and Lambdas

You can create anonymous functions inline and pass them directly as callbacks:

```js
fn apply_twice(val, operation) {
    return operation(operation(val));
}

var double = fn(x) { return x * 2; };
print(apply_twice(5, double));

var res = apply_twice(10, fn(x) { return x + 1; });
print(res);
```

---

## 6. Closures and Lexical Scope

Functions capture variables from their outer enclosing scope by reference:

```js
fn create_counter(start_value = 0) {
    var count = start_value;
    return fn() {
        count = count + 1;
        return count;
    };
}

var counter_a = create_counter(0);
var counter_b = create_counter(100);

print(counter_a());
print(counter_a());
print(counter_b());
```

---

## 7. Recursion

RayQuiro handles recursive functions efficiently:

```js
fn fibonacci(n) {
    if (n <= 1) { return n; }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

var k = 0;
while (k <= 10) {
    print("fib(" + str(k) + ") = " + str(fibonacci(k)));
    k = k + 1;
}
```

---

## 8. Asynchronous Functions (`async fn` & `await`)

RayQuiro has asynchronous programming using the `async` and `await` keywords:

```js
async fn fetch_user_data(user_id) {
    var response = await http.get("https://api.example.com/users/" + str(user_id));
    return response.body;
}

async fn main() {
    print("Fetching data...");
    var data = await fetch_user_data(42);
    print("Received: " + str(data));
}
```

An `async fn` returns a Promise value that resolves when the function body completes or throws. Calling `await` unwraps the resolved value or throws if an error occurred. For a complete guide, see the [Asynchronous Programming](/language/async) documentation.
