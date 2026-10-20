---
title: net
description: Low-level cross-platform TCP socket communication in RayQuiro.
slug: 1.0/built-ins/net
---

The `net` namespace provides low-level TCP client socket primitives. No import is required.

***

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `net.tcp_connect` | `net.tcp_connect(host, port)` | `number` | Connects to a remote TCP server. Returns numeric socket handle (or `0` on error). |
| `net.tcp_send` | `net.tcp_send(handle, data)` | `bool` | Sends string data over the TCP socket. Returns `true` on success. |
| `net.tcp_recv` | `net.tcp_recv(handle, max_bytes)` | `string` | Receives incoming string data up to `max_bytes`. |
| `net.tcp_close` | `net.tcp_close(handle)` | `bool` | Closes the open TCP socket. |

***

## Complete Example

```js
var sock = net.tcp_connect("127.0.0.1", 8080);

if (sock != 0) {
    var httpRequest = "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n";
    net.tcp_send(sock, httpRequest);

    var response = net.tcp_recv(sock, 4096);
    print("Received response:\n" + response);

    net.tcp_close(sock);
} else {
    print("Connection failed!");
}
```
