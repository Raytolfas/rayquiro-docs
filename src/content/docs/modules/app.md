---
title: rayquiro.app
description: Application DOM elements (HTML-like) and desktop window lifecycle for RayQuiro.
---

The `rayquiro.app` module serves as the **HTML/DOM structure** layer of RayQuiro. Just as HTML provides semantic structure and elements (`<button>`, `<input>`, `<div>`) while CSS styles them, `rayquiro.app` creates and organizes UI element objects, while `rayquiro.ui` provides styling.

```rq
import "rayquiro.app";
import "rayquiro.ui";
```

---

## 1. The Mental Model: `app = HTML, ui = CSS`

```
┌────────────────────────────────────────────────────────┐
│                   RayQuiro Interface                   │
├──────────────────────────┬─────────────────────────────┤
│       rayquiro.app       │        rayquiro.ui          │
│      (HTML Elements)     │       (CSS & Styling)       │
├──────────────────────────┼─────────────────────────────┤
│ • Button, Text, Input    │ • Color palettes & themes   │
│ • Checkbox, Radio        │ • CSS rules & inline styles │
│ • Slider, Progress, Select│ • Margins, paddings, borders│
│ • Row, Column, Box, Card │ • Minimal default styles    │
│ • Window & Event Loop    │ • ui.apply(element, style)  │
└──────────────────────────┴─────────────────────────────┘
```

---

## 2. Element Catalog (`app.*`)

All element constructors return a clean, structured `Element` object.

| Element | Signature | Description |
|---------|-----------|-------------|
| **Button** | `app.button(text, options)` | Interactive push button (`<button>`). |
| **Text** | `app.text(text, options)` | Inline text label (`<span>` / `<label>`). |
| **Input** | `app.input(placeholder, value, options)` | Single-line text input field (`<input>`). |
| **Textarea** | `app.textarea(placeholder, value, options)` | Multi-line text area (`<textarea>`). |
| **Checkbox** | `app.checkbox(label, checked, options)` | Toggle checkbox (`<input type="checkbox">`). |
| **Radio** | `app.radio(label, group, checked, options)` | Radio selection button (`<input type="radio">`). |
| **Slider** | `app.slider(min, max, value, options)` | Numeric range slider (`<input type="range">`). |
| **Progress** | `app.progress(value, max, options)` | Progress status bar (`<progress>`). |
| **Select** | `app.select(optionsArray, selectedIndex, options)` | Dropdown select menu (`<select>`). |
| **Image** | `app.image(src, options)` | Image element (`<img>`). |
| **Link** | `app.link(url, text, options)` | Hyperlink anchor (`<a href="...">`). |
| **Heading** | `app.heading(text, level, options)` | Title heading `<h1>` - `<h6>`. |
| **Divider** | `app.divider(options)` | Horizontal rule separator (`<hr />`). |
| **Row** | `app.row(children, options)` | Horizontal flexbox layout (`display: flex; flex-direction: row`). |
| **Column** | `app.column(children, options)` | Vertical flexbox layout (`display: flex; flex-direction: column`). |
| **Box / Card** | `app.box(children, options)` | Container card/box (`<div>`). |
| **Generic** | `app.element(tag, props, children, style)` | Generic custom DOM element constructor. |
| **To HTML** | `app.to_html(element)` | Serializes element tree directly to valid HTML string. |

---

## 3. Creating & Organizing Elements

Elements can be created with clean, minimal default styles and composed into hierarchies:

```rq
import "rayquiro.app";
import "rayquiro.ui";

// 1. Create basic unstyled/clean elements (like pure HTML)
var title = app.heading("Вход в систему", 2);
var loginInput = app.input("Имя пользователя...");
var passInput = app.input("Пароль...");
var remember = app.checkbox("Запомнить меня", true);
var submitBtn = app.button("Войти", { "id": "btn_login" });

// 2. Apply clean CSS styles using rayquiro.ui
submitBtn = ui.apply(submitBtn, {
    "background": "#2563eb",
    "color": "#ffffff",
    "radius": 6,
    "padding": "8px 16px"
});

// 3. Compose layout using containers (Row / Column / Card)
var formCard = app.card([
    title,
    app.divider(),
    loginInput,
    passInput,
    remember,
    submitBtn
]);

// 4. Export or inspect as HTML
var htmlCode = app.to_html(formCard);
print(htmlCode);
```

---

## 4. Running Desktop Applications & Windows

The `app` module launches native desktop applications, opens OS windows, and manages native controls, while `ui` configures styling (backgrounds, fonts, colors, and CSS rules):

```rq
import "rayquiro.app";
import "rayquiro.ui";

app.init("My Desktop App", 480, 340);

ui.style("background: #18181b; color: #f4f4f5; font-size: 14;");

app.text("Welcome to RayQuiro Desktop Application!");
app.input("Enter your command...");
app.checkbox("Start automatically with OS", true);
app.button("Launch");

app.run();
```

### Window & Control APIs:

| Function | Description |
|----------|-------------|
| `app.init(title, width, height)` | Creates and displays an application window. |
| `app.run()` | Starts the OS message/event loop. |
| `app.button(text, x, y, w, h)` | Adds a button control (auto-positioned if coordinates are omitted). |
| `app.text(text, x, y, w, h)` | Adds a text label control. |
| `app.input(placeholder, x, y, w, h)` | Adds a single-line text input control. |
| `app.checkbox(label, checked, x, y, w, h)` | Adds a toggle checkbox control. |
| `app.msg(title, text)` | Displays a native modal message dialog box. |
| `app.quit()` / `app.close()` | Closes the window and terminates the app. |