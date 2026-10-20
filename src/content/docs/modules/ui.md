---
title: rayquiro.ui
description: UI styling, themes, design system presets, CSS parser, and color manipulation module for RayQuiro.
---

The `rayquiro.ui` module is the official design and styling system for RayQuiro. It provides theme palettes (Dark, Light, Nord, Dracula, Cyberpunk, Midnight), custom theme generation, CSS-like stylesheet parsing and formatting, color arithmetic (`blend`, `lighten`, `darken`, `alpha`), and component styling presets for buttons, cards, typography, and inputs.

```rq
import "rayquiro.ui";
```

---

## 1. Quick Reference

| Category | Functions | Description |
|----------|-----------|-------------|
| **Themes** | `ui.theme(name)`, `ui.dark()`, `ui.light()`, `ui.nord()`, `ui.dracula()`, `ui.cyberpunk()`, `ui.midnight()` | Preconfigured color palettes and typography defaults. |
| **Theme Creation** | `ui.create_theme(options)` | Creates a custom theme extending a base palette. |
| **Color Math** | `ui.rgb(r, g, b)`, `ui.rgba(r, g, b, a)`, `ui.hex(color)` | Formats and converts color values. |
| **Color Adjustments**| `ui.blend(c1, c2, factor)`, `ui.lighten(c, factor)`, `ui.darken(c, factor)`, `ui.alpha(c, opacity)` | Linear interpolation, lightness tuning, and alpha channels. |
| **Component Styles**| `ui.button_style(variant, opts)`, `ui.card_style(opts)`, `ui.text_style(role, opts)`, `ui.badge_style(variant, opts)`, `ui.input_style(opts)` | Generates styled component configuration objects. |
| **CSS Stylesheets**| `ui.parse(cssString)`, `ui.stringify(styleObj)`, `ui.style(cssString)` | Bidirectional CSS parser, generator, and active sheet setter. |

---

## 2. Themes & Color Palettes

### Built-in Themes

RayQuiro includes built-in design themes ready for instant usage:

```rq
import "rayquiro.ui";

var nord = ui.theme("nord");
print(nord["background"]);
print(nord["primary"]);

var dark = ui.dark();
var light = ui.light();
var dracula = ui.dracula();
var cyberpunk = ui.cyberpunk();
var midnight = ui.midnight();
```

### Theme Structure

Every theme object exposes standardized design tokens:

```json
{
  "name": "nord",
  "background": "#2e3440",
  "surface": "#3b4252",
  "border": "#434c5e",
  "text": "#eceff4",
  "textMuted": "#d8dee9",
  "primary": "#88c0d0",
  "primaryHover": "#81a1c1",
  "secondary": "#4c566a",
  "success": "#a3be8c",
  "warning": "#ebcb8b",
  "danger": "#bf616a",
  "radius": 8,
  "font": "Segoe UI"
}
```

### Custom Theme Creation (`ui.create_theme`)

You can extend an existing palette by overriding specific tokens:

```rq
import "rayquiro.ui";

var myBrandTheme = ui.create_theme({
    "base": "dark",
    "primary": "#ff4400",
    "primaryHover": "#e03d00",
    "radius": 14,
    "font": "Fira Code"
});

print(myBrandTheme["primary"]);
print(myBrandTheme["background"]);
```

---

## 3. Color Arithmetic & Utilities

The `rayquiro.ui` module provides utilities for calculating dynamic colors, hover states, gradients, and transparencies:

### `ui.rgb` and `ui.rgba`

```rq
var orange = ui.rgb(255, 128, 0);
var translucent = ui.rgba(0, 0, 0, 0.5);
```

### `ui.blend`

Linearly blends two colors by a factor from `0.0` (100% color 1) to `1.0` (100% color 2):

```rq
var gray = ui.blend("#000000", "#ffffff", 0.5);
var softRed = ui.blend("#ffffff", "#ff0000", 0.2);
```

### `ui.lighten` and `ui.darken`

Calculates lighter or darker tints for hover, active, or disabled states:

```rq
var baseColor = "#3b82f6";
var hoverColor = ui.lighten(baseColor, 0.15);
var pressedColor = ui.darken(baseColor, 0.15);
```

### `ui.alpha`

Extracts the RGB channels from a hex color and applies an opacity level:

```rq
var transparentPrimary = ui.alpha("#3b82f6", 0.2);
```

---

## 4. Component Style Helpers

Rather than hardcoding CSS or raw hex strings everywhere, use component style presets:

### Button Styles (`ui.button_style`)

Supported variants: `"primary"`, `"secondary"`, `"danger"`, `"success"`, `"ghost"`, `"outline"`.

```rq
import "rayquiro.ui";

var dangerBtn = ui.button_style("danger");
print(dangerBtn["background"]);
print(dangerBtn["foreground"]);

var customBtn = ui.button_style("primary", {
    "radius": 20,
    "padding": "10px 24px"
});
```

### Card Styles (`ui.card_style`)

```rq
var card = ui.card_style({
    "background": "#1e1e24",
    "radius": 16,
    "padding": "24px"
});
```

### Text & Typography Styles (`ui.text_style`)

Supported roles: `"title"`, `"subtitle"`, `"body"`, `"caption"`, `"code"`.

```rq
var title = ui.text_style("title");
print(title["size"]);
print(title["weight"]);

var code = ui.text_style("code");
print(code["font"]);
```

### Badges & Form Inputs

```rq
var badge = ui.badge_style("success");
var input = ui.input_style({ "radius": 8 });
```

---

## 5. CSS Stylesheet Parser & Stringifier

The `rayquiro.ui` engine can parse CSS declarations into RayQuiro objects, or serialize RayQuiro objects into valid CSS strings:

### Parsing CSS (`ui.parse`)

```rq
import "rayquiro.ui";

var css = "
.btn-submit {
    background: #3b82f6;
    border: none;
    radius: 8px;
}
.card {
    background: #27272a;
    padding: 16px;
}
";

var sheet = ui.parse(css);
print(sheet[".btn-submit"]["background"]);
print(sheet[".card"]["padding"]);
```

### Stringifying Objects to CSS (`ui.stringify`)

```rq
var styles = {
    ".dialog": {
        "background": "#111827",
        "border": "1px solid #374151"
    }
};

var cssText = ui.stringify(styles);
print(cssText);
```

---

## 6. Complete Example: Themed Desktop Application

Here is an example combining `rayquiro.ui` for styling and `rayquiro.app` for native window rendering:

```rq
import "rayquiro.app";
import "rayquiro.ui";

var theme = ui.theme("midnight");
var headerText = ui.text_style("title", { "color": theme["primary"] });
var actionBtn = ui.button_style("primary", { "background": theme["primary"] });

var win = app.window({
    title: "Themed Application Shell",
    width: 900,
    height: 600,
    resizable: true
});

print("Active Theme: " + theme["name"]);
print("Window Title Color: " + headerText["color"]);
print("Button Accent: " + actionBtn["background"]);

while (win.isOpen()) {
    win.pollEvents();
}
```
