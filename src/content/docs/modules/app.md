---
title: rayquiro.app
description: Application DOM elements, pixel-perfect native desktop GUI, and window lifecycle for RayQuiro.
---

The `rayquiro.app` module serves as the primary UI structural foundation for RayQuiro. It operates in two unified modes:

1. **Native Desktop GUI Application**: Native Win32/Linux windowing, High-DPI awareness, automatic pixel-perfect baseline alignment, built-in themes, and event loop management.
2. **Declarative DOM/HTML Elements**: Component hierarchy building (`<button>`, `<input>`, `<div>`, flex rows/columns) and serialization to HTML via `app.to_html`.

```rq
import "rayquiro.app";
import "rayquiro.ui";
```

---

## 1. The Mental Model: `app = HTML / Controls, ui = CSS`

```
┌────────────────────────────────────────────────────────┐
│                   RayQuiro Interface                   │
├──────────────────────────┬─────────────────────────────┤
│       rayquiro.app       │        rayquiro.ui          │
│    (Controls & Structure)│       (CSS & Styling)       │
├──────────────────────────┼─────────────────────────────┤
│ • Window Lifecycle       │ • Themes: dark, light, nord │
│ • High-DPI Awareness     │ • Colors: rgb, rgba, hex    │
│ • Button, Text, Input    │ • Color blending & alpha    │
│ • Checkbox, Radio, Slider│ • CSS rule parser           │
│ • Row, Column, Box, Card │ • ui.apply(element, style)  │
│ • app.to_html(element)   │ • Typography & tokens       │
└──────────────────────────┴─────────────────────────────┘
```

---

## 2. Native Desktop GUI Applications

In v1.1, `rayquiro.app` features full High-DPI support (`SetProcessDPIAware`) on Windows and pixel-perfect vertical centering across both Windows and Linux. All controls adhere to a standardized 36px height baseline, eliminating layout jumping and misaligned fonts.

```rq
import "rayquiro.app";
import "rayquiro.ui";

app.init("RayQuiro v1.1 Studio", 520, 380);

app.set_theme("dark");

app.text("Welcome to RayQuiro Desktop Application");
app.input("Project name or path...");
app.checkbox("Enable Vulkan PBR hardware acceleration", true);
app.button("Create Project");

app.run();
```

### Desktop Window & Controls API

| Function | Signature | Description |
|----------|-----------|-------------|
| `app.init` | `app.init(title, width, height)` | Initializes application window with High-DPI scaling enabled. |
| `app.run` | `app.run()` | Starts OS event processing and render loop. |
| `app.set_theme` | `app.set_theme(name)` | Applies theme palette (`"dark"`, `"light"`, `"midnight"`, `"dracula"`, `"cyberpunk"`). |
| `app.set_style` | `app.set_style(cssLike)` | Configures background and font size via CSS syntax. |
| `app.button` | `app.button(text, x = -1, y = -1, w = -1, h = -1)` | Native push button with auto-layout or explicit geometry. |
| `app.text` | `app.text(text, x = -1, y = -1, w = -1, h = -1)` | Vertically centered text label aligning with buttons and inputs. |
| `app.input` | `app.input(placeholder, x = -1, y = -1, w = -1, h = -1)` | Single-line editable text input box with clipboard support. |
| `app.checkbox` | `app.checkbox(label, checked, x = -1, y = -1, w = -1, h = -1)` | Native toggle checkbox with vertically centered baseline. |
| `app.msg` | `app.msg(title, text)` | Native modal system message dialog box. |
| `app.show_message` | `app.show_message(title, text)` | Alias for `app.msg`. |
| `app.quit` | `app.quit()` | Terminates message loop and destroys application window. |

---

## 3. Declarative DOM & HTML Elements

`rayquiro.app` can also be used as a structured UI element tree generator that serializes directly to clean HTML:

| Element | Signature | Description |
|---------|-----------|-------------|
| **Button** | `app.button(text, options)` | Interactive button element (`<button>`). |
| **Text** | `app.text(text, options)` | Text span / label element (`<span>`). |
| **Label** | `app.label(text, options)` | Form label element (`<label>`). |
| **Input** | `app.input(placeholder, value, options)` | Text input field (`<input>`). |
| **Textarea** | `app.textarea(placeholder, value, options)` | Multi-line text field (`<textarea>`). |
| **Checkbox** | `app.checkbox(label, checked, options)` | Toggle checkbox (`<input type="checkbox">`). |
| **Radio** | `app.radio(label, group, checked, options)` | Radio button (`<input type="radio">`). |
| **Slider** | `app.slider(min, max, value, options)` | Numeric range slider (`<input type="range">`). |
| **Progress** | `app.progress(value, max, options)` | Progress bar (`<progress>`). |
| **Select** | `app.select(optionsArray, selectedIndex, options)` | Dropdown select menu (`<select>`). |
| **Image** | `app.image(src, options)` | Image element (`<img>`). |
| **Link** | `app.link(url, text, options)` | Anchor hyperlink (`<a href="...">`). |
| **Heading** | `app.heading(text, level, options)` | Heading element `<h1>` - `<h6>`. |
| **Divider** | `app.divider(options)` | Horizontal divider line (`<hr />`). |
| **Row** | `app.row(children, options)` | Horizontal flexbox layout container. |
| **Column** | `app.column(children, options)` | Vertical flexbox layout container. |
| **Box** | `app.box(children, options)` | Container block (`<div>`). |
| **Card** | `app.card(children, options)` | Styled card container. |
| **Generic** | `app.element(tag, props, children, style)` | Generic custom HTML tag constructor. |
| **To HTML** | `app.to_html(element)` | Serializes element tree directly to HTML string. |

### Component Composition Example

```rq
import "rayquiro.app";
import "rayquiro.ui";

var heading = app.heading("Account Login", 2);
var userField = app.input("Username");
var passField = app.input("Password");
var keepLogged = app.checkbox("Remember session", true);
var loginBtn = app.button("Sign In");

loginBtn = ui.apply(loginBtn, {
    "background": "#2563eb",
    "color": "#ffffff",
    "radius": 6,
    "padding": "8px 16px"
});

var card = app.card([
    heading,
    app.divider(),
    userField,
    passField,
    keepLogged,
    loginBtn
]);

var html = app.to_html(card);
print(html);
```
