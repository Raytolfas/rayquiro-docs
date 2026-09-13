---
title: Installation
description: Install RayQuiro on Windows and Linux.
---

## Windows

```powershell
irm rq.raytolfas.cc | iex
```

Installs `rqio` and adds it to PATH.

```bash
rqio version
```

## Linux

```bash
curl -fsSL rq.raytolfas.cc/linux | bash
```

## Build from source

**Windows** (needs MinGW g++):

```powershell
git clone https://github.com/raytolfas/rayquiro
cd rayquiro
powershell -ExecutionPolicy Bypass -File build.ps1
```

**Linux** (needs GCC 10+):

```bash
git clone https://github.com/raytolfas/rayquiro
cd rayquiro
bash build.sh && sudo cp rqio /usr/local/bin/
```

## VS Code Extension

[marketplace.visualstudio.com/items?itemName=raytolfas.rayquiro-lang](https://marketplace.visualstudio.com/items?itemName=raytolfas.rayquiro-lang)

Or search **RayQuiro** in the Extensions panel.
