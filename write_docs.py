import os, pathlib

BASE = r"G:\Projects\1projects\rayquiro-docs\src\content\docs"

def w(rel, txt):
    p = os.path.join(BASE, rel)
    pathlib.Path(p).parent.mkdir(parents=True, exist_ok=True)
    open(p, "w", encoding="utf-8").write(txt)
    print("wrote", rel)

w("getting-started/installation.md", """\
---
title: Installation
description: How to install RayQuiro on Windows and Linux.
---

## Windows

1. Download `rqio.exe` from [GitHub Releases](https://github.com/raytolfas/rayquiro/releases)
2. Place it in e.g. `C:\\\\rqio\\\\` and add to PATH

```bash
rqio version
# RayQuiro 0.2.0
```

### Build from source

```powershell
git clone https://github.com/raytolfas/rayquiro
cd rayquiro
powershell -ExecutionPolicy Bypass -File build.ps1
```

## Linux

```bash
git clone https://github.com/raytolfas/rayquiro
cd rayquiro
bash build.sh
sudo cp rqio /usr/local/bin/
rqio version
```

## VS Code Extension

Install the `.vsix` from [GitHub Releases](https://github.com/raytolfas/rayquiro/releases):

```
Extensions → ... → Install from VSIX → rayquiro-0.1.0.vsix
```
""")

w("getting-started/hello-world.md", """\
---
title: Hello, World!
description: Write your first RayQuiro program.
---

## Simplest program

```js
print("Hello, World!");
```

```bash
rqio run hello.rq
# Hello, World!
```

## With a function

```js
fn greet(name) {
    return "Hello, " + name + "!";
}
print(greet("RayQuiro"));
```

## Async entry point

```js
async fn main() {
    var now = datetime.now();
    print("Year: " + str(now?.["year"]));
    print("ID: " + crypto.uuid());
}
main();
```

| Line | Meaning |
|------|---------|
| `fn greet(name)` | Function with one parameter |
| `return "Hello, " + name` | String concatenation |
| `print(...)` | Print to stdout + newline |
| `async fn main()` | Async function |
| `datetime.now()` | Built-in, no import needed |
| `crypto.uuid()` | Built-in, no import needed |
""")

w("getting-started/project-structure.md", """\
---
title: Project Structure
description: How a RayQuiro project is organized.
---

## Initialize

```bash
rqio init my-project
cd my-project
rqio run main.rq
```

Creates:

```
my-project/
  main.rq        entry point
  rqio.json      project manifest
```

## rqio.json

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "main": "main.rq",
  "dependencies": {
    "colors": "raytolfas/rq-colors"
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Project name |
| `version` | string | Semver version |
| `main` | string | Entry point file |
| `dependencies` | object | name to owner/repo |

## Packages

- Global: `~/.rqio/packages/<name>/`
- Local: `./.rqio/packages/<name>/`

## Build

```bash
rqio build main.rq -o myapp
rqio build main.rq --release
```
""")

w("language/syntax.md", """\
---
title: Syntax
description: Core syntax rules of RayQuiro.
---

## Variables

```js
var name = "Alice";
var age  = 25;
var flag = true;
var none = null;
```

## Constants

```js
const PI  = 3.14159;
const MAX = 100;
```

## Comments

```js
// Line comment
/* Block comment */
var x = 1; // inline
```

## Semicolons — optional

```js
var a = 1
var b = 2
print(a + b)
```

## Identifiers

Start with letter or `_`: `myVar`, `_private`, `MAX_SIZE`

## Strings

```js
var s1 = "hello";
var s2 = 'world';
// escapes: \\n \\t \\\\ \\" \\'
```

## Numbers

```js
var i = 42;
var f = 3.14;
var h = 0xFF;
```

## Truthiness

Falsy: `null`, `false`, `0`, `""`
Everything else is truthy.
""")

w("language/types.md", """\
---
title: Types
description: Built-in data types in RayQuiro.
---

## number

64-bit float. All numeric literals.

```js
var x = 42;
var y = 3.14;
type(x)   // "number"
```

Math: `abs`, `sqrt`, `floor`, `ceil`, `round`, `pow`, `min`, `max`

## string

UTF-8 string.

```js
var s = "hello";
len(s)        // 5
s + " world"  // "hello world"
str(42)       // "42"
```

## bool

```js
var t = true;
var f = false;
bool(1)    // true
bool(0)    // false
bool("")   // false
```

## null

```js
var x = null;
x == null        // true
x ?? "default"   // "default"
```

## array

```js
var arr = [1, 2, "three"];
arr[0]            // 1
len(arr)          // 3
push(arr, 4)
pop(arr)
slice(arr, 1, 3)
```

## object

```js
var obj = { name: "Alice", age: 30 };
obj["name"]     // "Alice"
keys(obj)       // ["name", "age"]
values(obj)     // ["Alice", 30]
```

## Type inspection

```js
type(42)    // "number"
type("hi")  // "string"
type(true)  // "bool"
type(null)  // "null"
type([])    // "array"
type({})    // "object"
```

## Conversion

```js
num("42")    // 42
str(100)     // "100"
bool(0)      // false
```
""")

w("language/functions.md", """\
---
title: Functions
description: Declaring and using functions in RayQuiro.
---

## Basic

```js
fn add(a, b) {
    return a + b;
}
print(add(3, 4));   // 7
```

## Default parameters via ??

```js
fn greet(name, prefix) {
    prefix = prefix ?? "Hello";
    return prefix + ", " + name + "!";
}
greet("Alice")         // "Hello, Alice!"
greet("Bob", "Hi")     // "Hi, Bob!"
```

## Multiple return values

```js
fn divmod(a, b) {
    return a / b, a % b;
}
var res = divmod(10, 3);
var q   = res?.["0"];   // 3.333
var r   = res?.["1"];   // 1
```

## Closures

```js
fn makeCounter() {
    var n = 0;
    return fn() { n = n + 1; return n; };
}
var c = makeCounter();
c();  // 1
c();  // 2
```

## Anonymous functions

```js
var square = fn(x) { return x * x; };
square(7);   // 49
```

## Async

```js
async fn fetchData(url) {
    return await http.get(url);
}
async fn main() {
    var data = await fetchData("https://example.com");
    print(data?.["body"]);
}
main();
```

## Recursion

```js
fn fib(n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
fib(10);   // 55
```
""")

w("language/control-flow.md", """\
---
title: Control Flow
description: if, while, for, break, continue, match.
---

## if / else if / else

```js
if (score >= 90) {
    print("A");
} else if (score >= 70) {
    print("B");
} else {
    print("C");
}
```

## while

```js
var i = 0;
while (i < 5) {
    print(i);
    i = i + 1;
}
```

## for / in (array)

```js
for fruit in ["apple", "banana"] {
    print(fruit);
}
```

## range loop

```js
for i in range(0, 10) {
    print(i);
}
```

## break / continue

```js
for i in range(0, 100) {
    if (i == 5) break;
    if (i % 2 == 0) continue;
    print(i);
}
```

## match

```js
match status {
    200 => print("OK"),
    404 => print("Not Found"),
    _   => print("Unknown"),
}
```

String match:

```js
match cmd {
    "start" => print("Starting"),
    "stop"  => print("Stopping"),
    _       => print("Unknown: " + cmd),
}
```
""")

w("language/error-handling.md", """\
---
title: Error Handling
description: try, catch, throw and error patterns.
---

## try / catch

```js
try {
    var x = riskyOp();
} catch (err) {
    print("Error: " + str(err));
}
```

## throw any value

```js
fn divide(a, b) {
    if (b == 0) throw "Division by zero";
    return a / b;
}
```

## throw an object

```js
throw { code: "NOT_FOUND", message: "Resource not found" };
```

```js
try {
    validate(-5);
} catch (e) {
    print(e?.["message"]);
}
```

## Re-throwing

```js
try {
    op();
} catch (e) {
    if (e == "fatal") throw e;
    print("Handled: " + str(e));
}
```

## Nested try/catch

```js
try {
    try {
        throw "inner";
    } catch (i) {
        print("inner: " + i);
        throw "outer";
    }
} catch (o) {
    print("outer: " + o);
}
```
""")

w("language/operators.md", """\
---
title: Operators
description: All operators in RayQuiro.
---

## Arithmetic

| Op | Description | Example |
|----|-------------|---------|
| `+` | Add / concat | `3+4` = `7`, `"a"+"b"` = `"ab"` |
| `-` | Subtract | `10-3` = `7` |
| `*` | Multiply | `2*5` = `10` |
| `/` | Divide | `7/2` = `3.5` |
| `%` | Modulo | `7%3` = `1` |
| `++` | Post-increment | `i++` |
| `--` | Post-decrement | `i--` |

## Assignment

`=`, `+=`, `-=`, `*=`, `/=`, `%=`

## Comparison

`==`, `!=`, `<`, `>`, `<=`, `>=`

## Logical

`&&`, `||`, `!`

## Null Coalescing `??`

Returns right side when left is `null`:

```js
var name = null;
name ?? "Anonymous"   // "Anonymous"

var port = env.get("PORT") ?? "3000";
```

## Optional Chaining `?.`

Safe property access — returns `null` instead of throwing:

```js
var user = null;
user?.["name"]          // null, no error

getUser()?.["profile"]?.["avatar"]
```

## Index access `[]`

```js
arr[0]       // array index
obj["key"]   // object key
```
""")

w("language/modules.md", """\
---
title: Modules
description: Importing local files and packages.
---

## Built-ins (no import)

Always available:

```js
json.parse(...)
datetime.now()
crypto.uuid()
path.join(...)
process.exit(0)
env.get("HOME")
hash.sha256("text")
fs.read("file.txt")
```

## Local file import

```js
import "lib/utils.rq";
print(formatDate(datetime.now()));
```

Path is relative to current file.

## Package import

After `rqio add colors`:

```js
import "colors";
print(colors.red("error!"));
```

## Exports

All top-level `fn`, `var`, `const` are auto-exported:

```js
// lib/math.rq
fn square(x) { return x * x; }
const E = 2.71828;
```

```js
// main.rq
import "lib/math.rq";
print(square(5));   // 25
print(E);           // 2.71828
```
""")

w("built-ins/json.md", """\
---
title: json
description: JSON parsing and serialization.
---

Built-in — no import required.

## json.parse(str)

Parses JSON string to a RayQuiro value.

```js
var data = json.parse('{"name":"Alice","age":30}');
data?.["name"]   // "Alice"
data?.["age"]    // 30

json.parse("[1,2,3]")   // array
json.parse("42")        // 42
json.parse("true")      // true
```

Throws on invalid JSON.

## json.stringify(value)

Converts any value to JSON string.

```js
json.stringify({ name: "Bob", scores: [10,20] })
// '{"name":"Bob","scores":[10,20]}'

json.stringify(null)    // "null"
json.stringify(42)      // "42"
json.stringify([1,"x"]) // '[1,"x"]'
```

## Round-trip

```js
var obj = { users: [{ id: 1, name: "Alice" }] };
var back = json.parse(json.stringify(obj));
back?.["users"]?.[0]?.["name"]   // "Alice"
```
""")

w("built-ins/process.md", """\
---
title: process
description: Process information and control.
---

Built-in — no import required.

## process.args()

Returns command-line arguments as an array of strings.

```bash
rqio run script.rq hello world
```

```js
var args = process.args();
// ["hello", "world"]
print(args[0]);   // "hello"
```

## process.exit(code)

Exits the process with the given code (0 = success).

```js
if (args[0] == null) {
    print("Usage: script.rq <name>");
    process.exit(1);
}
```

## process.pid()

Returns the current process ID as a number.

```js
print(process.pid());   // 12345
```

## process.cwd()

Returns the current working directory.

```js
print(process.cwd());   // "/home/user/project"
```
""")

w("built-ins/datetime.md", """\
---
title: datetime
description: Date and time functions.
---

Built-in — no import required.

## datetime.now()

Returns current local date/time as an object.

| Field | Type | Example |
|-------|------|---------|
| `year` | number | 2025 |
| `month` | number | 8 |
| `day` | number | 28 |
| `hour` | number | 14 |
| `minute` | number | 30 |
| `second` | number | 0 |
| `ms` | number | 500 |
| `timestamp` | number | Unix timestamp |

```js
var now = datetime.now();
now?.["year"]       // 2025
now?.["timestamp"]  // 1724846400
```

## datetime.timestamp()

Returns Unix timestamp (seconds since epoch).

```js
var ts = datetime.timestamp();
print(ts);   // 1724846400
```

## datetime.format(timestamp, pattern)

Formats a Unix timestamp with strftime pattern.

```js
var ts = datetime.timestamp();
datetime.format(ts, "%Y-%m-%d")           // "2025-08-28"
datetime.format(ts, "%H:%M:%S")           // "14:30:00"
datetime.format(ts, "%A, %B %d %Y")       // "Thursday, August 28 2025"
datetime.format(ts, "%Y-%m-%dT%H:%M:%SZ") // ISO 8601
```

| Spec | Meaning |
|------|---------|
| `%Y` | 4-digit year |
| `%m` | Month 01-12 |
| `%d` | Day 01-31 |
| `%H` | Hour 00-23 |
| `%M` | Minute 00-59 |
| `%S` | Second 00-59 |
| `%A` | Weekday name |
| `%B` | Month name |
""")

w("built-ins/path.md", """\
---
title: path
description: File path utilities.
---

Built-in — no import required.

## path.join(...parts)

Joins path parts with OS separator.

```js
path.join("src", "lib", "utils.rq")  // "src/lib/utils.rq"
path.join("/home", "user", ".rqio")  // "/home/user/.rqio"
```

## path.basename(p)

Filename including extension.

```js
path.basename("/home/user/main.rq")   // "main.rq"
```

## path.dirname(p)

Directory part.

```js
path.dirname("/home/user/main.rq")   // "/home/user"
```

## path.ext(p)

File extension with dot.

```js
path.ext("main.rq")    // ".rq"
path.ext("README")     // ""
```

## path.stem(p)

Filename without extension.

```js
path.stem("main.rq")   // "main"
```

## path.exists(p)

Returns `true` if path exists on filesystem.

```js
path.exists("main.rq")   // true or false
```

## path.abs(p)

Absolute path resolved from cwd.

```js
path.abs("lib/utils.rq")   // "/home/user/project/lib/utils.rq"
```
""")

w("built-ins/fs.md", """\
---
title: fs
description: File system operations.
---

Built-in — no import required.

## fs.read(path)

Reads file contents as a string. Throws if not found.

```js
var content = fs.read("data.json");
var data = json.parse(content);
```

## fs.write(path, content)

Writes string to file (overwrites).

```js
fs.write("output.txt", "Hello!");
fs.write("log.json", json.stringify({ ts: datetime.timestamp() }));
```

## fs.exists(path)

Returns `true` if file or directory exists.

```js
if (fs.exists("config.json")) {
    var cfg = json.parse(fs.read("config.json"));
}
```

## fs.mkdir(path)

Creates directory and all parents.

```js
fs.mkdir("output/reports");
fs.write("output/reports/2025.txt", "data");
```

## fs.readdir(path)

Returns array of filenames in directory.

```js
var files = fs.readdir(".");
for f in files { print(f); }
```

## fs.remove(path)

Deletes file or directory.

```js
fs.remove("temp.txt");
fs.remove("build/");
```
""")

w("built-ins/env.md", """\
---
title: env
description: Environment variable access.
---

Built-in — no import required.

## env.get(name)

Returns env var value or `""` if not set.

```js
var home = env.get("HOME");
var port = env.get("PORT") ?? "3000";
```

## env.set(name, value)

Sets env var for the current process.

```js
env.set("MY_APP_ENV", "production");
```

## env.has(name)

Returns `true` if the variable is set.

```js
if (env.has("CI")) {
    print("Running in CI");
}
```

## env.all()

Returns all env vars as an object.

```js
var all = env.all();
for k in keys(all) {
    print(k + "=" + all[k]);
}
```

## Example

```js
var cfg = {
    host:  env.get("DB_HOST") ?? "localhost",
    port:  num(env.get("DB_PORT") ?? "5432"),
    debug: env.has("DEBUG"),
};
```
""")

w("built-ins/hash.md", """\
---
title: hash
description: Hashing functions.
---

Built-in — no import required. Also available as `crypto.sha256` / `crypto.sha1`.

## hash.sha256(str)

SHA-256 hash — returns 64-char hex string.

```js
hash.sha256("hello")
// "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
```

## hash.sha1(str)

SHA-1 hash — returns 40-char hex string.

```js
hash.sha1("hello")
// "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"
```

## Use cases

```js
var checksum = hash.sha256(fs.read("package.zip"));
var cacheKey = hash.sha256(json.stringify(params));
```

> For passwords, use `crypto.hmac_sha256` with a secret key.
""")

w("built-ins/crypto.md", """\
---
title: crypto
description: Cryptographic utilities — built-in, no import needed.
---

All functions run natively in the VM. No external dependencies.

## crypto.sha256(str)

SHA-256 — alias for `hash.sha256`.

```js
crypto.sha256("hello")
// "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
```

## crypto.sha1(str)

SHA-1 — alias for `hash.sha1`.

```js
crypto.sha1("hello")
// "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"
```

## crypto.md5(str)

MD5 — returns 32-char hex string.

```js
crypto.md5("hello")
// "5d41402abc4b2a76b9719d911017c592"
```

> MD5 is not secure for passwords. Use for checksums only.

## crypto.base64_encode(str)

Encodes string to Base64.

```js
crypto.base64_encode("RayQuiro!")
// "UmF5UXVpcm8h"
```

## crypto.base64_decode(str)

Decodes Base64 to original string.

```js
crypto.base64_decode("UmF5UXVpcm8h")
// "RayQuiro!"
```

Round-trip:

```js
var enc = crypto.base64_encode("Hello!");
crypto.base64_decode(enc)   // "Hello!"
```

## crypto.uuid()

Random UUID v4.

```js
crypto.uuid()
// "a1b2c3d4-e5f6-4789-abcd-ef0123456789"
```

Each call returns a different UUID.

## crypto.random_bytes(n)

`n` random bytes as hex string (length = `n * 2`). Max 1024 bytes.

```js
crypto.random_bytes(8)    // "a3f7219c4b8e0d56"
crypto.random_bytes(32)   // 64-char hex token
```

## crypto.hmac_sha256(message, key)

HMAC-SHA256 — keyed hash for authentication. Returns 64-char hex.

```js
crypto.hmac_sha256("message body", "my-secret-key")
// "8b5f48702995c1598c573db1e21866a9b825d4a794d169d7060a03605796360b"
```

Verify:

```js
fn verify(body, key, expected) {
    return crypto.hmac_sha256(body, key) == expected;
}
```

> Use for API signing, webhook verification, token generation.
""")

w("package-manager/init.md", """\
---
title: rqio init
description: Initialize a new RayQuiro project.
---

```bash
rqio init [folder]
```

Creates `main.rq` + `rqio.json` in the given folder (or current dir).

```bash
rqio init my-app
cd my-app
rqio run main.rq
```

Generated `rqio.json`:

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "main": "main.rq"
}
```
""")

w("package-manager/add.md", """\
---
title: rqio add
description: Add and install a package.
---

```bash
rqio add <name>
rqio add <owner/repo>
rqio add <owner/repo@branch>
rqio add <name> --local
```

## Examples

```bash
rqio add colors
rqio add raytolfas/rq-colors
rqio add raytolfas/rq-colors@dev
```

Installs globally to `~/.rqio/packages/` and adds to `rqio.json`.

With `--local`: installs to `./.rqio/packages/`.

## After adding

```js
import "colors";
print(colors.red("Error!"));
```
""")

w("package-manager/install.md", """\
---
title: rqio install
description: Install all dependencies from rqio.json.
---

```bash
rqio install          # install all from rqio.json
rqio install <name>   # install one package
```

## Example

`rqio.json`:

```json
{
  "dependencies": {
    "colors": "raytolfas/rq-colors",
    "args":   "raytolfas/rq-args"
  }
}
```

```bash
rqio install
# installs colors and args
```
""")

w("package-manager/remove.md", """\
---
title: rqio remove
description: Remove an installed package.
---

```bash
rqio remove <name>
rqio remove <name> --local
```

Removes from `~/.rqio/packages/` (or `.rqio/packages/` with `--local`) and from `rqio.json`.

```bash
rqio remove colors
# Removed 'colors'
```
""")

w("package-manager/list.md", """\
---
title: rqio list
description: List installed packages.
---

```bash
rqio list
```

Output:

```
Installed packages (~/.rqio/packages/):
  colors    raytolfas/rq-colors
  args      raytolfas/rq-args
```
""")

w("package-manager/rqio-json.md", """\
---
title: rqio.json
description: Project manifest format.
---

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "main": "main.rq",
  "description": "My project",
  "author": "Alice",
  "license": "MIT",
  "dependencies": {
    "colors": "raytolfas/rq-colors"
  }
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `name` | yes | Project name |
| `version` | yes | Semver string |
| `main` | yes | Entry `.rq` file |
| `description` | no | Short description |
| `author` | no | Author name |
| `license` | no | License |
| `dependencies` | no | name to owner/repo |
""")

w("cli/run.md", """\
---
title: rqio run
description: Run a RayQuiro script.
---

```bash
rqio run <file.rq> [args...]
rqio run <file.rq> --legacy
rqio run <file.rq> --vm
```

Default: uses **Bytecode VM**. Falls back to interpreter for unsupported features.

| Flag | Description |
|------|-------------|
| `--legacy` | Force tree-walk interpreter |
| `--vm` | Force VM (fails on unsupported) |

## Arguments

```bash
rqio run app.rq hello world
```

```js
var args = process.args();
// ["hello", "world"]
```

## Exit codes

`0` = success, `1` = runtime error, `2` = file not found
""")

w("cli/build.md", """\
---
title: rqio build
description: Compile to a native binary.
---

```bash
rqio build <file.rq>
rqio build <file.rq> -o <output>
rqio build <file.rq> --release
rqio build <file.rq> --debug
```

| Flag | Compiler flags | Description |
|------|---------------|-------------|
| (none) | `-O2 -s` | Default |
| `--release` | `-O3 -s -flto` | Max optimization |
| `--debug` | `-O0 -g` | With debug symbols |

## Examples

```bash
rqio build main.rq
rqio build main.rq -o myapp --release
```

The binary is standalone — no rqio runtime needed to run it.

Requires: g++ on PATH (MinGW on Windows, GCC on Linux).
""")

w("cli/fmt.md", """\
---
title: rqio fmt
description: Format a RayQuiro source file.
---

```bash
rqio fmt <file.rq>
```

Formats the file in-place: consistent indentation, spacing, style.

```bash
rqio fmt main.rq
# Formatted main.rq
```
""")

w("cli/debug.md", """\
---
title: rqio debug
description: DAP debugger for VS Code.
---

```bash
rqio debug <file.rq>
rqio debug <file.rq> --port 5678
```

Starts a DAP server and waits for a debugger client.

## VS Code launch.json

```json
{
  "version": "0.2.0",
  "configurations": [{
    "name": "RayQuiro Debug",
    "type": "debugpy",
    "request": "launch",
    "program": "\${workspaceFolder}/main.rq",
    "runtimeExecutable": "rqio",
    "runtimeArgs": ["debug"],
    "port": 5678
  }]
}
```

Press **F5** to debug.

Supports: breakpoints, variable inspection, step over/into/out, call stack.
""")

w("guides/vs-code.md", """\
---
title: VS Code Extension
description: Syntax highlighting, snippets and run commands.
---

## Install

1. Download `rayquiro-0.1.0.vsix` from [GitHub Releases](https://github.com/raytolfas/rayquiro/releases)
2. **Extensions** → `...` → **Install from VSIX**

## Features

- Syntax highlighting for `.rq` / `.rqio`
- Snippets: `fn`, `afn`, `var`, `if`, `ife`, `for`, `while`, `try`, `import`, `struct`, `enum`, `main`...
- **Ctrl+F5** — run current file
- **Ctrl+Shift+B** — build current file
- Right-click any `.rq` in Explorer → **RayQuiro: Run File**

## Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `rayquiro.rqioPath` | `rqio` | Path to rqio binary |
| `rayquiro.buildArgs` | `""` | Extra build flags |

Example in `settings.json`:

```json
{
  "rayquiro.rqioPath": "C:/rqio/rqio.exe",
  "rayquiro.buildArgs": "--release"
}
```
""")

w("guides/cross-platform.md", """\
---
title: Cross-Platform
description: Writing code that works on Windows and Linux.
---

RayQuiro code is 100% cross-platform. The same `.rq` file runs identically on both.

## Path separators

```js
// Use path.join — not hardcoded separators
var p = path.join("src", "lib", "utils.rq");
```

## Home directory

```js
var home = env.get("HOME") ?? env.get("USERPROFILE") ?? ".";
```

## OS detection

```js
var isWindows = env.get("OS") == "Windows_NT";
```

## Line endings

Normalize with:

```js
var content = fs.read("file.txt");
content = str.replace(content, "\\r\\n", "\\n");
```

## Build

| Platform | Command |
|----------|---------|
| Windows | `powershell -File build.ps1` |
| Linux | `bash build.sh` |

Binaries: `.exe` on Windows, no extension on Linux. `rqio build` handles automatically.
""")

w("guides/performance.md", """\
---
title: Performance
description: Making RayQuiro programs faster.
---

## Execution modes

| Mode | Command | Speed |
|------|---------|-------|
| Native binary | `rqio build --release` | Fastest |
| Bytecode VM | `rqio run` | Fast |
| Tree-walk | `rqio run --legacy` | Slower |

## Build for production

```bash
rqio build main.rq --release
./main
```

Uses `-O3 -s -flto`.

## Tips

1. Use `path.join` instead of string concatenation for paths
2. Cache `len(arr)` before loops
3. `crypto.*` runs natively in VM — no fallback penalty
4. Use arrays for performance-critical iteration

## Timing

```js
var start = datetime.timestamp();
// ... code ...
print("Elapsed: " + str(datetime.timestamp() - start) + "s");
```
""")

# ── Styles / tsconfig ─────────────────────────────────────────────────────────

styles = r"G:\Projects\1projects\rayquiro-docs\src\styles"
pathlib.Path(styles).mkdir(parents=True, exist_ok=True)
open(os.path.join(styles, "custom.css"), "w").write("""\
:root {
  --sl-color-accent:       #6366f1;
  --sl-color-accent-high:  #818cf8;
  --sl-color-accent-low:   #4f46e5;
}
""")
print("wrote styles/custom.css")

open(r"G:\Projects\1projects\rayquiro-docs\tsconfig.json", "w").write("""\
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": { "strictNullChecks": true }
}
""")
print("wrote tsconfig.json")

print("\\nALL DOCS DONE")
