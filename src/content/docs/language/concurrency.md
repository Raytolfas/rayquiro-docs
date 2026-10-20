---
title: Concurrency & Channels
description: Lightweight thread execution with spawn and thread-safe channels in RayQuiro 1.0.
---

RayQuiro 1.0 provides concurrency primitives: `spawn` for background execution and `channel()` for message passing between threads.

---

## 1. Spawning Threads (`spawn`)

The `spawn` keyword executes a function, closure, or callable in a background thread:

```rq
spawn fn() {
    print("Running in background thread!")
}

fn worker(id) {
    print("Worker running:", id)
}

spawn worker(1)
spawn worker(2)
```

Execution continues immediately on the main thread without blocking.

---

## 2. Channels (`channel()`)

Channels allow thread-safe bidirectional communication between spawned threads and the main thread.

### Creating a Channel

```rq
var ch = channel()
```

### Sending Messages (`send`)

```rq
spawn fn() {
    var result = 40 + 2
    ch.send(result)
}
```

You can also use the functional helper:
```rq
channel.send(ch, "data")
```

### Receiving Messages (`recv`)

The `recv()` method blocks until a message is available on the channel:

```rq
var msg = ch.recv()
print("Received:", msg)
```

Or using functional syntax:
```rq
var msg = channel.recv(ch)
```

### Closing a Channel (`close`)

```rq
ch.close()
```

---

## 3. Producer-Consumer Example

```rq
var queue = channel()

spawn fn() {
    for (i = 1; i <= 5; i++) {
        queue.send("Task #" + str(i))
    }
}

for (i = 1; i <= 5; i++) {
    var task = queue.recv()
    print("Processing:", task)
}
```
