---
title: Publishing Packages
description: How to distribute and publish RayQuiro packages via GitHub and the official registry.
---

RayQuiro packages are natively distributed through Git repositories and indexed by the official RayQuiro Registry (`rq.raytolfas.cc`).

---

## 1. Direct Distribution via GitHub

Any public GitHub repository containing an `rqio.json` can be installed immediately by any RayQuiro developer worldwide.

### Step 1: Initialize Git and Push

```bash
cd my-math
git init
git add .
git commit -m "feat: initial release"
git remote add origin https://github.com/username/my-math.git
git branch -M main
git push -u origin main
```

### Step 2: Tag a Release

RayQuiro's package manager resolves versions using Git tags. Tag your commit with the matching version from `rqio.json`:

```bash
git tag v1.0.0
git push origin v1.0.0
```

### Step 3: Users Install Directly

Users can now install your package globally or per-project:

```bash
# Global installation:
rqio add username/my-math

# Local project installation:
rqio add username/my-math --local
```

---

## 2. Submitting to the Official Registry

Packages in the official registry can be installed using short names: `rqio add my-math`.

### Submission Requirements

1. **Manifest:** Complete `rqio.json` with required keys: `name`, `version`, `description`, `entry`, `license`.
2. **Documentation:** Informative `README.md` with installation and API usage examples.
3. **Tags:** At least one Git tag matching the manifest version (e.g. `v1.0.0`).
4. **License:** Recognized open-source license.

### Submission Steps

1. Visit the registry repository: `https://github.com/Raytolfas/Assets`.
2. Open a Pull Request adding your package to `RayQuiro/frameworks.json`:
   ```json
   {
     "name": "my-math",
     "repo": "https://github.com/username/my-math",
     "description": "Essential mathematical algorithms and vector utilities",
     "category": "math"
   }
   ```
3. Once the automated validation CI passes and the PR is merged, your package is indexed on `rq.raytolfas.cc`.

---

## 3. Releasing Updates

When updating your package:

1. Update `"version"` in `rqio.json` (e.g. `"1.1.0"`).
2. Commit and push:
   ```bash
   git commit -am "release: v1.1.0"
   git tag v1.1.0
   git push origin main --tags
   ```
3. Consumers update their installed dependencies with:
   ```bash
   rqio install
   ```