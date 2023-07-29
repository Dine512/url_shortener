# Cервис генерации короткой ссылки
## Локальный запуск
### Установка зависимостей
```commandline
pip install -r requirements.txt
```
### Настройка
Создайте файл .env и добавьте туда следующие настройки:
```
PG_HOST = хост postgersql
PG_PORT = порт postgersql
PG_USER = имя пользователя postgersql
PG_PASS = пароль для postgersql
PG_NAME = название базы postgersql
```
По желанию можно указать
```
SHORT_URL_LENGTH = длина короткой ссылки
SERVICE_URL = доменное имя сервиса
```
### Запуск API
Для запуска API, в консоли нужно выполнить:
```
./run
```
## Запуск через Docker

### Настройка переменных окружения
В файле docker-compose.yml выставить переменные окружения в секции pg (PG_HOST менять не нужно):
```
PG_USER: postgres
PG_PASS: postgres  # change on production
PG_NAME: postgres
```

В секции api выставить переменные окружения такие же как в секции pg
```
PG_USER: postgres
PG_PASSWORD: postgres # change on production
PG_DATABASE: postgres
```
### Сборка и запуск контейнеров
Для соборки и запуска контейнера выполните в командной строке:
```commandline
 docker-compose up --build -d
```