# Cервис генерации короткой ссылки
## Установка зависимостей
```commandline
pip install -r requirements.txt
```
## Настройка
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