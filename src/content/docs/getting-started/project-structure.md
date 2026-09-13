---
title: Project Structure
description: How a RayQuiro project is organized.
---

```bash
rqio init my-project
cd my-project
rqio run main.rq
```

```
my-project/
  main.rq       entry point
  rqio.json     manifest
```

## rqio.json

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "main": "main.rq",
  "dependencies": {}
}
```
