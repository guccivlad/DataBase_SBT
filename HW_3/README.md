## 1. Развернули CouchDB в Docker
С помощью команды
```bach
docker run -p 5984:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin -d couchdb:3.2
```
запустили контейнер в Docker

![](Docker.jpg)

## 2. База данных

Перешли по ссылке ```http://localhost:5984/_utils``` и создали базу данных И добавили поле имя:

![](Create_db_1.jpg)

![](Create_db_2.jpg)

## 3. Инсталяция

В фафле ```ДЗ3.html``` прописали путь к инсталяции:
```
Remote: new PouchDB('http://admin:admin@localhost:5984/db')
```

## 4. Запуск
Запустили ```ДЗ3.html``` и нажали кнопку sync:

![](result.jpg)

Далее остановили CouchDB сервер:

![](db_stop.jpg)

И убедились, что в файле ```ДЗ3.html``` по-прежнему фигурирует наше имя:

![](after_update.jpg)