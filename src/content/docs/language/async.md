---
title: Asynchronous Programming
description: Complete guide to async fn, await, Promises, and asynchronous operations in RayQuiro.
---

RayQuiro provides built-in support for asynchronous, non-blocking execution using `async fn` and `await`. This enables handling network requests, timers, and heavy tasks concurrently without freezing application execution or the UI message loop.

---

## 1. The `async` Keyword

Declaring a function with `async fn` marks it as asynchronous. Asynchronous functions always return a Promise representing their eventual result:

```js
async fn compute_result() {
    return 42;
}

var promise = compute_result();
print(promise); // <Promise>
```

---

## 2. Awaiting Promises (`await`)

Inside an `async fn` or at the top level of a script, you can use `await` to pause execution until a Promise resolves or rejects:

```js
async fn load_greeting(name) {
    time.sleep(50);
    return "Hello, " + name + "!";
}

async fn run() {
    print("Loading...");
    var msg = await load_greeting("RayQuiro");
    print(msg); // Hello, RayQuiro!
}

run();
```

---

## 3. Error Handling with `try` / `catch`

Rejections and thrown exceptions inside asynchronous functions can be caught cleanly using standard `try` / `catch` blocks:

```js
async fn fetch_api(url) {
    if (len(url) == 0) {
        throw "Invalid URL provided";
    }
    return await http.get(url);
}

async fn safe_fetch() {
    try {
        var res = await fetch_api("");
        print(res.body);
    } catch (err) {
        print("Caught async error: " + str(err));
    }
}

safe_fetch();
```

---

## 4. Concurrent Requests & Asynchronous Built-ins

Built-in modules such as `http` provide asynchronous operations that pair with `await`:

```js
async fn fetch_all() {
    var req1 = http.get("https://api.example.com/status");
    var req2 = http.get("https://api.example.com/metrics");

    var res1 = await req1;
    var res2 = await req2;

    print("Status code: " + str(res1.status));
    print("Metrics: " + str(res2.body));
}
```

---

## 5. Summary

| Feature | Syntax | Description |
|---------|--------|-------------|
| Async Function | `async fn name(...) { ... }` | Defines a function returning a Promise. |
| Await | `await promise` | Pauses current execution until the promise resolves. |
| Try/Catch | `try { await ... } catch (e) { ... }` | Captures exceptions thrown during asynchronous execution. |
