CW7_tracker_of_habits

## Описание
Этот проект представляет собой API-сервер для сервиса отслеживания полезных привычек. Проект позволяет создавать,
изменять, просматривать и удалять полезные привычки и пользователей. Проект предусматривает отправку
сообщений через telegram-бота по IP-пользователя.

## Установка
Клонируйте проэкт с GitHub

This should clone this project from Github:
```
git clone https://github.com/oleg2300x/CourseWork_7
```
Установите необходимые библиотеки:
```
pip install -r requirements.txt
```
When that is said and done, that should be it on the computer side, you should connect this service with Database.

## Переменные окружения
Для работы приложения необходимо создать файл ".env" с вашими данными.
Все данные которые нужно внести находятся в файле ".env-sample".
Для отправки рабочего сообщения в Telegram вам нужен токен Telegram-бота.
```
PASSWORD=
SECRET_KEY=
CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
TELEGRAM_BOT_API_KEY=
```

## Подключение к базе данных
Установите PosgreSQL. 
```
https://www.postgresql.org/download/
```

Затем создайте базу данных.
```
CREATE DATABASE name_database
```

Затем вы должны выполнить миграцию с помощью этих команд
```
python manage.py makemigrations
```
```
python manage.py migrate
```

## Celery
Для правильной работы Celery вам нужен Redis. После загрузки Redis вы можете запустить worker. Для этого вам следует использовать команду
```
celery -A config beat -l info
```

## Создание суперпользователя
Для создания суперпользователя вам следует использовать команду
```
python manage.py csu
```

## Документация
Всю документацию о конечных точках вы можете посмотреть по ссылке
```
http://localhost:8000/docs/
http://localhost:8000/redoc/
```
## Развёртывание проэкта 
Для развертывания проекта после клонирования и создания файла .env вам необходимо установить docker и docker-compose.
Затем вы можете использовать команды
```
docker-compose build
docker-compose up
```

или
```
docker-compose up -d —build
```