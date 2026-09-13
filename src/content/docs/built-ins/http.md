---
title: http
description: Performing outbound HTTP requests, GET, POST, custom headers, and JSON responses.
---

The `http` namespace allows RayQuiro programs to communicate with REST APIs, fetch web content, and post payloads over HTTP/HTTPS.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `http.get` | `http.get(url, headers)` | `object` | Performs an HTTP GET request. |
| `http.post` | `http.post(url, body, headers)` | `object` | Performs an HTTP POST request. |
| `http.request` | `http.request(options)` | `object` | Generic configurable HTTP request. |

---

## Response Object Structure

HTTP requests return an object with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `status` | `number` | HTTP status code (e.g. `200`, `404`, `500`). |
| `body` | `string` | Raw body text returned by the server. |
| `headers` | `object` | Map of response headers received. |

---

## Examples

### Performing a GET Request

```js
var res = http.get("https://api.github.com/repos/raytolfas/rayquiro", {
    "User-Agent": "RayQuiro-Client/0.2.0"
});

if (res["status"] == 200) {
    var repo = json.parse(res["body"]);
    print("Repository Stars: " + str(repo["stargazers_count"]));
} else {
    print("Request failed with HTTP status: " + str(res["status"]));
}
```

---

### Sending a POST Request with JSON Payload

```js
var payload = json.stringify({
    title: "Bug report",
    body: "Found an unexpected token error",
    priority: "high"
});

var res = http.post("https://example.com/api/tickets", payload, {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + env.get("API_TOKEN")
});

print("Response status: " + str(res["status"]));
print("Response body: " + res["body"]);
```