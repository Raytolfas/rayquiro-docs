---
title: Error Handling
description: Exceptions, throw, try/catch/finally blocks, and error management in RayQuiro.
---

RayQuiro includes native exception handling via `throw` and `try / catch / finally` blocks across both the Bytecode VM and native LLVM binaries.

---

## 1. Throwing Errors (`throw`)

You can throw any value as an error (strings, numbers, objects):

```js
fn divide(a, b) {
    if (b == 0) {
        throw "Division by zero error";
    }
    return a / b;
}
```

---

## 2. Catching Errors (`try / catch`)

Catch runtime errors, division by zero, invalid JSON, or missing files:

```js
try {
    var result = divide(10, 0);
    print("Result: " + str(result));
} catch (err) {
    print("Caught an error: " + err);
}
```

---

## 3. The `finally` Clause

The `finally` block executes unconditionally after the `try` and `catch` blocks finish, regardless of whether an exception occurred:

```js
fn process_transaction() {
    var db_conn = db.open("app.db");
    try {
        db_conn.exec("BEGIN TRANSACTION;");
        db_conn.exec("INSERT INTO logs VALUES ('started');");
        // risky code
        db_conn.exec("COMMIT;");
    } catch (e) {
        db_conn.exec("ROLLBACK;");
        print("Transaction failed: " + e);
    } finally {
        db_conn.close();
        print("Connection safely closed.");
    }
}
```

---

## 4. Structured Error Objects

You can throw structured objects containing error codes, timestamps, and stack details:

```js
fn validate_user(user) {
    if (!user.has("email")) {
        throw {
            code: "ERR_MISSING_FIELD",
            field: "email",
            message: "User object requires an email property"
        };
    }
}

try {
    validate_user({ name: "John" });
} catch (err) {
    if (type(err) == "object") {
        print("Error Code: " + err["code"] + " (" + err["message"] + ")");
    } else {
        print("Error: " + str(err));
    }
}
```