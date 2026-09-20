---
title: db
description: Embedded SQLite database queries, parameterized statements, and transactions.
slug: 0.2.1/built-ins/db
---

The `db` namespace provides lightweight, zero-configuration embedded relational database capabilities using SQLite.

***

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `db.open` | `db.open(path)` | `database` | Opens or creates an embedded database file. |
| `database.exec` | `database.exec(sql)` | `void` | Executes a DDL or modification statement. |
| `database.query` | `database.query(sql, params)` | `array` | Runs a query and returns matched rows as an array of objects. |
| `database.close` | `database.close()` | `void` | Closes the database connection. |

***

## Complete Example

```js
// Open or create database file (use ":memory:" for in-memory DB)
var conn = db.open("app.db");

// Create schema
conn.exec("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, score INTEGER);");

// Insert rows with parameter bindings (prevents SQL injection)
conn.exec("INSERT INTO users (name, score) VALUES ('Alice', 120);");
conn.exec("INSERT INTO users (name, score) VALUES ('Bob', 95);");

// Query rows
var rows = conn.query("SELECT * FROM users WHERE score > ? ORDER BY score DESC;", [100]);

var i = 0;
while (i < len(rows)) {
    var user = rows[i];
    print("User: " + user["name"] + " — Score: " + str(user["score"]));
    i = i + 1;
}

conn.close();
```
