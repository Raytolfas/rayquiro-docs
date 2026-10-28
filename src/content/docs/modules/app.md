---
title: rayquiro.app
description: Declarative Slint hardware-accelerated desktop UI, native OS windowing, and DOM element tree for RayQuiro.
---

The `rayquiro.app` module serves as the primary UI structural foundation for RayQuiro applications. In RayQuiro 1.3, it operates in three integrated modes:

1. **Declarative Slint Desktop Applications**: GPU-accelerated desktop UI rendered via Slint. Builds complete component trees directly in RayQuiro without external `.slint` files.
2. **Native Desktop GUI Applications**: Native Win32/Linux desktop windowing with High-DPI awareness, standardized baseline controls, and modal dialogs.
3. **Declarative DOM/HTML Elements**: Component hierarchy construction and serialization to HTML strings via `app.to_html`.

```rq
import "rayquiro.app";
import "rayquiro.ui";
```

---

## 1. The Mental Model: `app = Controls & Structure, ui = Styling`

```
┌────────────────────────────────────────────────────────┐
│                   RayQuiro Interface                   │
├──────────────────────────┬─────────────────────────────┤
│       rayquiro.app       │        rayquiro.ui          │
│    (Controls & Structure)│       (CSS & Styling)       │
├──────────────────────────┼─────────────────────────────┤
│ • Slint Hardware Engine  │ • Themes: dark, light, nord │
│ • Native OS Windowing    │ • Colors: rgb, rgba, hex    │
│ • Button, Text, Input    │ • Color blending & alpha    │
│ • Textarea, Slider, Box  │ • CSS rule parser           │
│ • Row, Column, Card      │ • ui.apply(element, style)  │
│ • app.to_slint(element)  │ • Typography & tokens       │
│ • app.to_html(element)   │ • Layout constraints        │
└──────────────────────────┴─────────────────────────────┘
```

---

## 2. Declarative Slint Desktop Applications

RayQuiro 1.3 includes full Slint integration. You define the complete layout, cards, buttons, text inputs, sliders, and controls directly in RayQuiro syntax. The runtime compiles the tree into optimized Slint component definitions in memory and launches the hardware-accelerated window.

### Declarative Slint Example

```rq
import "rayquiro.app";

var header = app.row([
    app.column([
        app.heading("RayQuiro Studio", 2),
        app.text("Declarative desktop application written entirely in pure RayQuiro")
    ]),
    app.button("Sync State")
]);

var cardMetrics = app.card([
    app.heading("Execution Metrics", 3),
    app.text("Engine: Bytecode VM / LLVM Native"),
    app.text("Memory: 38.2 MB managed heap"),
    app.text("Latency: 0.14ms GC cycle")
]);

var cardControls = app.card([
    app.heading("Configuration", 3),
    app.checkbox("Hardware Acceleration", true),
    app.checkbox("Realtime Profiler", false),
    app.text("Thread Pool Size:"),
    app.slider(1, 64, 16),
    app.text("Working Directory:"),
    app.input("Enter project path...", "")
]);

var mainLayout = app.column([
    header,
    app.divider(),
    app.row([cardMetrics, cardControls])
]);

app.run({
    title: "RayQuiro Studio",
    width: 900,
    height: 640,
    content: mainLayout
});
```

### Slint Engine Methods

| Function | Signature | Description |
|----------|-----------|-------------|
| `app.run` | `app.run(config)` | Launches Slint hardware-accelerated window. `config` accepts `title`, `width`, `height`, and `content`. |
| `app.to_slint` | `app.to_slint(element, config)` | Generates complete Slint component source markup from the element tree for inspection. |
| `app.has_slint` | `app.has_slint()` | Returns `true` if the local Slint execution engine is available. |
| `app.slint_check` | `app.slint_check(element)` | Performs syntax and semantic validation of the generated Slint component tree without opening a window. |
| `app.slint_screenshot` | `app.slint_screenshot(element, outPath)` | Headless rendering of the component tree directly into a PNG image file. |

---

## 3. UI Component Constructors

All UI elements can be used both in declarative Slint desktop apps and in HTML export:

| Element | Signature | Description |
|---------|-----------|-------------|
| **Button** | `app.button(text, options)` | Interactive push button. |
| **Text** | `app.text(text, options)` | Text label. |
| **Heading** | `app.heading(text, level, options)` | Header title (`level` 1 through 6). |
| **Input** | `app.input(placeholder, value, options)` | Single-line editable text input field. |
| **Textarea** | `app.textarea(placeholder, value, options)` | Multi-line text edit container. |
| **Checkbox** | `app.checkbox(label, checked, options)` | Boolean toggle checkbox. |
| **Slider** | `app.slider(min, max, value, options)` | Range slider control. |
| **Progress** | `app.progress(value, max, options)` | Visual progress bar indicator. |
| **Divider** | `app.divider(options)` | Horizontal separator line. |
| **Row** | `app.row(children, options)` | Horizontal layout container (`HorizontalLayout`). |
| **Column** | `app.column(children, options)` | Vertical layout container (`VerticalLayout`). |
| **Card** | `app.card(children, options)` | Elevated card panel with dark background and border. |
| **Box** | `app.box(children, options)` | Generic container block with padding and border. |
| **Select** | `app.select(optionsArray, selectedIndex, options)` | Dropdown selection control. |
| **Link** | `app.link(url, text, options)` | Hyperlink anchor element. |
| **Image** | `app.image(src, options)` | Image view element. |
| **Generic** | `app.element(tag, props, children, style)` | Generic custom UI element constructor. |

---

## 4. Native Desktop GUI Applications (OS Windowing)

For lightweight, zero-dependency system utility windows, `rayquiro.app` provides direct native Win32/Linux desktop windowing:

```rq
import "rayquiro.app";
import "rayquiro.ui";

app.init("RayQuiro Utility", 520, 380);
app.set_theme("dark");

app.text("System Diagnostics");
app.input("Filter query...");
app.checkbox("Verbose logging", true);
app.button("Execute");

app.run();
```

### Native OS Windowing API

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

## 5. Declarative DOM & HTML Export

The same element hierarchy created with `app.row`, `app.column`, `app.card`, etc., can be serialized directly to HTML:

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
