---
title: rayquiro.ui
description: Modern declarative cross-platform GUI framework for RayQuiro.
slug: 0.2.1/modules/ui
---

The `rayquiro.ui` module allows building fast, cross-platform desktop interfaces using a declarative, component-based layout model with reactive events.

```js
import "rayquiro.ui";
```

***

## 1. UI Components Catalog

| Component | Signature | Description |
|-----------|-----------|-------------|
| `ui.label` | `ui.label(text)` | Static or dynamic text display widget. |
| `ui.button` | `ui.button(text, on_click)` | Clickable push button with action callback. |
| `ui.textField` | `ui.textField(options)` | Single-line editable text input box. |
| `ui.checkbox` | `ui.checkbox(label, checked, on_change)` | Toggleable checkbox option. |
| `ui.slider` | `ui.slider(min, max, value, on_change)` | Continuous or discrete range slider. |
| `ui.row` | `ui.row(children)` | Horizontal flex layout container. |
| `ui.column` | `ui.column(children)` | Vertical stack layout container. |
| `ui.render` | `ui.render(root_component)` | Mounts and draws the component tree. |

***

## 2. Declarative Form Example

```js
import "rayquiro.ui";

var username = "";
var email = "";
var is_admin = false;

var form = ui.column([
    ui.label("Create User Account"),
    
    ui.row([
        ui.label("Username:"),
        ui.textField({
            placeholder: "Enter username...",
            onChange: fn(val) { username = val; }
        })
    ]),
    
    ui.row([
        ui.label("Email:"),
        ui.textField({
            placeholder: "name@domain.com",
            onChange: fn(val) { email = val; }
        })
    ]),
    
    ui.checkbox("Administrator privileges", false, fn(checked) {
        is_admin = checked;
    }),
    
    ui.button("Submit", fn() {
        print("Submitting: " + username + " (" + email + ") - Admin: " + str(is_admin));
    })
]);

ui.render(form);
```
