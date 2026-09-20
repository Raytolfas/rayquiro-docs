---
title: rayquiro.ui
description: Современный декларативный GUI фреймворк для RayQuiro.
---

Модуль `rayquiro.ui` позволяет разрабатывать быстрые нативные настольные приложения с декларативным описанием интерфейса и реактивной обработкой событий.

```js
import "rayquiro.ui";
```

---

## 1. Каталог компонентов UI

| Компонент | Сигнатура | Описание |
|-----------|-----------|----------|
| `ui.label` | `ui.label(text)` | Отображение текстовой метки. |
| `ui.button` | `ui.button(text, on_click)` | Нажимаемая кнопка с функцией обратного вызова. |
| `ui.textField` | `ui.textField(options)` | Однострочное поле ввода текста (`placeholder`, `onChange`). |
| `ui.checkbox` | `ui.checkbox(label, checked, on_change)` | Флажок переключателя с текстовой подписью. |
| `ui.slider` | `ui.slider(min, max, value, on_change)` | Ползунок диапазона числовых значений. |
| `ui.row` | `ui.row(children)` | Горизонтальный контейнер компоновки. |
| `ui.column` | `ui.column(children)` | Вертикальный контейнер компоновки. |
| `ui.render` | `ui.render(root_component)` | Монтирует дерево компонентов в окно и запускает цикл событий. |

---

## 2. Пример декларативной формы

```js
import "rayquiro.ui";

var username = "";
var email = "";
var is_admin = false;

var form = ui.column([
    ui.label("Создание учетной записи"),
    
    ui.row([
        ui.label("Имя пользователя:"),
        ui.textField({
            placeholder: "Введите имя...",
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
    
    ui.checkbox("Права администратора", false, fn(checked) {
        is_admin = checked;
    }),
    
    ui.button("Отправить", fn() {
        print("Отправка: " + username + " (" + email + ") - Админ: " + str(is_admin));
    })
]);

ui.render(form);
```