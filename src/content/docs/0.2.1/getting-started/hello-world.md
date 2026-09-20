---
title: Hello, World!
description: Your first RayQuiro program.
slug: 0.2.1/getting-started/hello-world
---

```js
print("Hello, World!");
```

```bash
rqio run hello.rq
```

## With a function

```js
fn greet(name) { return "Hello, " + name + "!"; }
print(greet("RayQuiro"));
```

## Async entry point

```js
async fn main() {
    var now = datetime.now();
    print("Year: " + str(now?.["year"]));
    print("ID: " + crypto.uuid());
}
main();
```
