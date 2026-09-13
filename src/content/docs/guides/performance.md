---
title: Performance Guide
description: Understanding execution modes, LLVM optimizations, memory usage, and writing high-performance RayQuiro code.
---

RayQuiro provides three distinct execution tiers to give you the ideal balance between instant development turnaround and production-grade execution speed.

---

## 1. Execution Tiers Compared

| Execution Mode | Command | Startup Latency | Execution Speed | Use Case |
|----------------|---------|-----------------|-----------------|----------|
| **Native Binary (LLVM)** | `rqio build --release` | Zero (direct native binary) | **Maximum** (C/Rust speed) | Production releases, games, desktop apps, servers |
| **Bytecode VM** | `rqio run script.rq` | Instant (~5ms) | **Fast** (JIT-like speed) | Daily development, rapid testing, scripts |
| **Tree-Walk Interpreter** | `rqio run --legacy` | Instant (~2ms) | Baseline | Debugging, embedded systems, microcontrollers |

---

## 2. LLVM Native Compilation

When you run:

```bash
rqio build main.rq --release -o app.exe
```

RayQuiro runs full LLVM compilation with `-O3`:
- Constant folding & propagation
- Inlining of small functions
- Dead code elimination (DCE)
- Loop unrolling and auto-vectorization
- Memory-to-register promotion (`mem2reg`)

The resulting binary executes directly on CPU registers with no virtual machine dispatch loop.

---

## 3. High-Performance Coding Tips

### 1. Cache Collection Lengths in Loops

In tight loops, cache `len(arr)` in a local variable:

```js
// Fast:
var n = len(items);
var i = 0;
while (i < n) {
    process(items[i]);
    i = i + 1;
}
```

### 2. Pre-allocate or Reuse Arrays

Avoid repeatedly creating temporary arrays inside hot inner loops.

### 3. Use Native Built-ins for Bulk Operations

Built-ins like `crypto.*`, `hash.*`, `regex.*`, and `math.*` execute in compiled C/C++ without VM overhead.

### 4. Benchmark with `time.ms()`

Always measure using monotonic timers:

```js
var t0 = time.ms();
compute_heavy_algorithm();
var delta = time.ms() - t0;
print("Computation time: " + str(delta) + " ms");
```