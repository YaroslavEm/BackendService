Чтобы инициализировать (импорт данных) БД нужно запустить файл search_article/get_json.py, предварительно закоментировав функцию сохранения в БД (Поле 69 save_categories(list_data))
Для запуска сервиса нужно установить интерпретатор python. Дополнительно нужно установить:
- Django командой pip install django
- DRF командой pip install rest_framework
- Перейти в папку проекта backend_developer\search_article
- Запустить сервер командой python manage.py runserver
- Перейти на URL http://127.0.0.1:8000/wiki/
