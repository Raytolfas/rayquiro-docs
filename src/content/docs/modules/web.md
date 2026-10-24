---
title: rayquiro.web
description: High-performance embedded HTTP web server, declarative component rendering, and routing for RayQuiro.
---

The `rayquiro.web` module provides both a native embedded HTTP server for REST APIs and a declarative component templating system for rendering HTML web applications with zero external dependencies.

```rq
import "rayquiro.web";
```

---

## 1. Declarative Web Components & Templating

In v1.1, `rayquiro.web` supports declarative element construction and templating without procedural nesting:

```rq
import "rayquiro.web";

var pageContent = web.element("div", {"class": "hero"}, [
    web.element("h1", {"class": "title"}, "Fast, Native Web"),
    web.element("p", {}, "Compiled directly to machine code"),
    web.element("button", {"class": "primary-btn"}, "Get Started")
]);

web.page("Home", pageContent);
```

### Declarative Methods

| Method | Signature | Description |
|--------|-----------|-------------|
| `web.element` | `web.element(tag, props, children)` | Constructs a declarative element node object. |
| `web.render` | `web.render(tree)` | Recursively compiles a component tree or string into HTML. |
| `web.template` | `web.template(html, data)` | Interpolates a data dictionary into an HTML string with `{{key}}` syntax. |
| `web.page` | `web.page(title, body, [path], [css])` | Generates a single complete HTML page file directly. |
| `web.begin` | `web.begin(title)` | Starts a multi-route static site build session. |
| `web.route` | `web.route(path, title)` | Defines a URL route and active page in static build. |
| `web.end` | `web.end()` | Finalizes and writes all static pages to the build directory. |

### Template Interpolation Example

```rq
import "rayquiro.web";

var templateString = "<div class=\"user-card\"><h2>{{name}}</h2><span>Role: {{role}}</span></div>";
var card = web.template(templateString, {
    "name": "RayQuiro Developer",
    "role": "Core Maintainer"
});

web.render(card);
```

---

## 2. Embedded HTTP Server & REST API

The HTTP server engine handles incoming TCP connections, parses HTTP/1.1 headers, and routes requests:

| Method | Signature | Description |
|--------|-----------|-------------|
| `web.server` | `web.server()` | Creates a new HTTP server instance. |
| `app.get` | `app.get(path, handler)` | Registers an HTTP GET route handler. |
| `app.post` | `app.post(path, handler)` | Registers an HTTP POST route handler. |
| `app.put` | `app.put(path, handler)` | Registers an HTTP PUT route handler. |
| `app.delete` | `app.delete(path, handler)` | Registers an HTTP DELETE route handler. |
| `app.static` | `app.static(prefix, dir)` | Serves static assets from a local folder. |
| `app.listen` | `app.listen(port)` | Starts the server listening on the specified port. |
| `app.stop` | `app.stop()` | Gracefully shuts down the web server. |

### Request & Response API

Inside a route handler `fn(req, res)`:

#### Request Object (`req`)

| Field | Type | Description |
|-------|------|-------------|
| `req.path` | `string` | The requested URL pathname. |
| `req.method` | `string` | HTTP verb (`"GET"`, `"POST"`, etc.). |
| `req.body` | `string` | Raw request body string. |
| `req.headers` | `object` | Key-value map of incoming HTTP headers. |
| `req.query` | `object` | Parsed query string parameters. |

#### Response Object (`res`)

| Method | Signature | Description |
|--------|-----------|-------------|
| `res.send` | `res.send(text)` | Sends plain text with status 200. |
| `res.html` | `res.html(html)` | Sends HTML text with `text/html; charset=utf-8`. |
| `res.json` | `res.json(obj)` | Serializes object to JSON with `application/json`. |
| `res.status` | `res.status(code)` | Sets the HTTP response status code. |
| `res.header` | `res.header(name, val)` | Sets a custom response header. |

---

## 3. REST API Example

```rq
import "rayquiro.web";

var app = web.server();

app.static("/public", "./public");

var items = [
    { id: 1, name: "Mechanical Keyboard", price: 120 },
    { id: 2, name: "Wireless Mouse", price: 65 }
];

app.get("/api/items", fn(req, res) {
    res.json({ success: true, count: len(items), data: items });
});

app.post("/api/items", fn(req, res) {
    try {
        var payload = json.parse(req.body);
        var new_item = {
            id: len(items) + 1,
            name: payload["name"],
            price: payload["price"]
        };
        items.push(new_item);

        res.status(201);
        res.json({ success: true, item: new_item });
    } catch (err) {
        res.status(400);
        res.json({ success: false, error: "Invalid JSON format" });
    }
});

app.get("/", fn(req, res) {
    res.html("<h1>RayQuiro Web Server</h1><p>Visit /api/items for REST data.</p>");
});

var port = 8080;
app.listen(port);
print("Web server running at http://localhost:" + str(port));
```
