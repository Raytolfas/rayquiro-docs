---
title: rayquiro.web
description: High-performance embedded HTTP web server and reactive routing for RayQuiro.
---

The `rayquiro.web` module provides a micro-web framework compiled natively into the RayQuiro binary. It allows you to build REST APIs, static web servers, and webhooks with zero external dependencies.

```js
import "rayquiro.web";
```

---

## 1. Quick Reference

| Method | Signature | Description |
|--------|-----------|-------------|
| `web.server` | `web.server()` | Creates a new HTTP server instance. |
| `app.get` | `app.get(path, handler)` | Registers an HTTP GET route. |
| `app.post` | `app.post(path, handler)` | Registers an HTTP POST route. |
| `app.put` | `app.put(path, handler)` | Registers an HTTP PUT route. |
| `app.delete` | `app.delete(path, handler)` | Registers an HTTP DELETE route. |
| `app.static` | `app.static(prefix, dir)` | Serves static assets from a local folder. |
| `app.listen` | `app.listen(port)` | Starts the server listening on the specified port. |
| `app.stop` | `app.stop()` | Gracefully shuts down the web server. |

---

## 2. Request and Response API

Inside a route handler `fn(req, res)`:

### Request Object (`req`)

| Field | Type | Description |
|-------|------|-------------|
| `req.path` | `string` | The requested URL pathname. |
| `req.method` | `string` | HTTP verb (`"GET"`, `"POST"`, etc.). |
| `req.body` | `string` | Raw request body string. |
| `req.headers` | `object` | Key-value map of incoming HTTP headers. |
| `req.query` | `object` | Parsed query string parameters. |

### Response Object (`res`)

| Method | Signature | Description |
|--------|-----------|-------------|
| `res.send` | `res.send(text)` | Sends plain text with status 200. |
| `res.html` | `res.html(html)` | Sends HTML text with `text/html; charset=utf-8`. |
| `res.json` | `res.json(obj)` | Serializes object to JSON with `application/json`. |
| `res.status` | `res.status(code)` | Sets the HTTP response status code. |
| `res.header` | `res.header(name, val)` | Sets a custom response header. |

---

## 3. Comprehensive REST API Example

```js
import "rayquiro.web";

var app = web.server();

// Serve static HTML/CSS/JS
app.static("/public", "./public");

// In-memory items database
var items = [
    { id: 1, name: "Mechanical Keyboard", price: 120 },
    { id: 2, name: "Wireless Mouse", price: 65 }
];

// GET /api/items
app.get("/api/items", fn(req, res) {
    res.json({ success: true, count: len(items), data: items });
});

// POST /api/items
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

// HTML Home route
app.get("/", fn(req, res) {
    res.html("<h1>RayQuiro Web Server</h1><p>Visit /api/items for REST data.</p>");
});

var port = 8080;
app.listen(port);
print("Web server running at http://localhost:" + str(port));
```