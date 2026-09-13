---
title: net
description: Low-level TCP and UDP client and server socket communication.
---

The `net` namespace provides primitives for building custom network servers and clients using standard BSD-style sockets.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `net.connect` | `net.connect(host, port)` | `socket` | Connects to a remote TCP server. |
| `net.listen` | `net.listen(port, on_conn)` | `server` | Binds and listens for incoming TCP connections. |
| `socket.send` | `socket.send(data)` | `number` | Sends string or bytes over the socket. |
| `socket.recv` | `socket.recv(max_bytes)` | `string` | Receives data from the socket. |
| `socket.close` | `socket.close()` | `void` | Closes the connection. |

---

## Examples

### Connecting to a TCP Server

```js
var sock = net.connect("echo.websocket.events", 80);

sock.send("GET / HTTP/1.1\r\nHost: echo.websocket.events\r\n\r\n");
var response = sock.recv(1024);

print("Received:\n" + response);
sock.close();
```

---

### Simple TCP Echo Server

```js
var server = net.listen(9000, fn(client) {
    print("New connection established!");
    
    var data = client.recv(1024);
    while (len(data) > 0) {
        client.send("ECHO: " + data);
        data = client.recv(1024);
    }
    
    client.close();
});
```