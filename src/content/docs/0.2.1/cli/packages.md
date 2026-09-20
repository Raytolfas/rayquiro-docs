---
title: Package Manager CLI
description: Full reference for rqio init, add, install, remove, and list commands.
slug: 0.2.1/cli/packages
---

RayQuiro includes a built-in package manager directly integrated into the `rqio` executable. It supports both local project dependencies and global tooling libraries.

***

## 1. Commands Overview

| Command | Syntax | Description |
|---------|--------|-------------|
| `init` | `rqio init [folder]` | Initializes a new project or package manifest (`rqio.json`). |
| `add` | `rqio add <pkg> [--local]` | Downloads and adds a dependency from the registry or GitHub. |
| `install` | `rqio install [pkg] [--local]` | Restores dependencies declared in `rqio.json`. |
| `remove` | `rqio remove <pkg> [--local]` | Uninstalls a package and updates manifest. |
| `list` | `rqio list [--global \| --local]` | Lists currently installed packages. |

***

## 2. Detailed Command Reference

### `rqio init [folder]`

Creates a fresh project directory structure with a template `rqio.json` manifest:

```bash
# In the current directory:
rqio init

# In a specific subfolder:
rqio init my-new-project
```

***

### `rqio add <name|owner/repo> [--local]`

Downloads and installs a package:

* **From Registry:** If a short name is specified (`telebot`), it searches the official index (`rq.raytolfas.cc`).
* **From GitHub:** If an `owner/repo` path is specified (`raytolfas/rq-colors`), it clones directly from GitHub.

```bash
# Install globally (default, accessible by all scripts):
rqio add telebot
rqio add raytolfas/rq-colors

# Install locally into the current project (.rqio/packages/):
rqio add telebot --local
```

When run in a project with an `rqio.json`, `rqio add` automatically records the package into the `"dependencies"` section of the manifest.

***

### `rqio install [name] [--local]`

* **Without arguments:** Scans `rqio.json` in the current directory and downloads all missing dependencies listed.
* **With a package name:** Installs the specific package.

```bash
# Clone a repository and install all its dependencies:
git clone https://github.com/example/rayquiro-app
cd rayquiro-app
rqio install
```

***

### `rqio remove <name> [--local]`

Removes an installed package from disk and deletes it from `rqio.json`:

```bash
# Remove from project:
rqio remove telebot --local

# Remove globally:
rqio remove telebot
```

***

### `rqio list [--global | --local]`

Displays all installed packages, their versions, and source paths:

```bash
rqio list
rqio list --local
rqio list --global
```

***

## 3. Storage Locations

| Scope | Windows Path | Linux / macOS Path |
|-------|--------------|-------------------|
| **Local** | `<project>/.rqio/packages/` | `<project>/.rqio/packages/` |
| **Global** | `%APPDATA%\rqio\packages\` | `~/.local/share/rqio/packages/` |
