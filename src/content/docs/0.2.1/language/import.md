---
title: Import
description: Importing files and packages.
slug: 0.2.1/language/import
---

## Built-ins — no import

`json`, `fs`, `env`, `datetime`, `crypto`, etc. are always available.

## Local file

```js
import "lib/utils.rq";
```

## Package

```js
import "telebot";
```

## Auto-export

All top-level `fn`, `var`, `const` are exported automatically.
