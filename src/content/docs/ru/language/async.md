---
title: Асинхронное программирование (async / await)
description: Полное руководство по асинхронным функциям, await, Promise и неблокирующим операциям в RayQuiro.
---

RayQuiro поддерживает асинхронное неблокирующее выполнение с помощью ключевых слов `async fn` и `await`. Это позволяет работать с сетью, таймерами и фоновыми задачами без блокировки основного потока приложения и оконного интерфейса.

---

## 1. Ключевое слово `async`

Объявление функции через `async fn` помечает её как асинхронную. Такая функция всегда возвращает объект `Promise`:

```rayquiro
async fn compute_result() {
    return 42;
}

var p = compute_result();
print(p);
```

---

## 2. Ожидание результата (`await`)

Внутри `async fn` или на верхнем уровне скрипта можно использовать оператор `await`, чтобы приостановить выполнение до тех пор, пока `Promise` не завершится успешным результатом или ошибкой:

```rayquiro
async fn load_greeting(name) {
    time.sleep(50);
    return "Привет, " + name + "!";
}

async fn run() {
    print("Загрузка данных...");
    var msg = await load_greeting("RayQuiro");
    print(msg);
}

run();
```

---

## 3. Обработка ошибок с `try` / `catch`

Ошибки и исключения, возникшие в асинхронных функциях, перехватываются стандартными блоками `try` / `catch`:

```rayquiro
async fn fetch_api(url) {
    if (len(url) == 0) {
        throw "Неверный URL адрес";
    }
    return await http.get(url);
}

async fn safe_fetch() {
    try {
        var res = await fetch_api("");
        print("Статус: " + str(res["status"]));
    } catch (err) {
        print("Перехвачена ошибка: " + str(err));
    }
}

safe_fetch();
```

---

## 4. Параллельное выполнение

Несколько асинхронных операций можно запускать параллельно, не дожидаясь завершения каждой по очереди:

```rayquiro
async fn task_one() {
    time.sleep(100);
    return "Задача 1 готова";
}

async fn task_two() {
    time.sleep(100);
    return "Задача 2 готова";
}

async fn main() {
    var p1 = task_one();
    var p2 = task_two();

    var res1 = await p1;
    var res2 = await p2;

    print(res1);
    print(res2);
}

main();
```
