---
title: db
description: Relational database connections, queries, scalar results, and SQL execution.
---

The `db` namespace provides relational database connectivity (PostgreSQL / SQLite connection string protocol) built into RayQuiro. No import is required.

---

## Quick Reference

| Function | Signature | Return Type | Description |
|----------|-----------|-------------|-------------|
| `db.connect` | `db.connect(conninfo)` | `number` | Opens connection. Returns a numeric connection handle (or `0` on error). |
| `db.query` | `db.query(handle, sql)` | `array` | Executes query and returns array of row objects. |
| `db.exec` | `db.exec(handle, sql)` | `number` | Executes SQL statement and returns number of affected rows. |
| `db.scalar` | `db.scalar(handle, sql)` | `any` | Returns the first column of the first row (or `null`). |
| `db.close` | `db.close(handle)` | `bool` | Closes the database connection. |

---

## Complete Example

```js
var conn = db.connect("host=localhost port=5432 dbname=app user=postgres password=secret");

if (conn != 0) {
    db.exec(conn, "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, score INT);");
    db.exec(conn, "INSERT INTO users (name, score) VALUES ('Alice', 100);");

    var rows = db.query(conn, "SELECT id, name, score FROM users ORDER BY score DESC;");
    var i = 0;
    while (i < len(rows)) {
        var row = rows[i];
        print("User: " + row["name"] + ", Score: " + str(row["score"]));
        i = i + 1;
    }

    var total = db.scalar(conn, "SELECT COUNT(*) FROM users;");
    print("Total users: " + str(total));

    db.close(conn);
} else {
    print("Failed to connect to database");
}
```
