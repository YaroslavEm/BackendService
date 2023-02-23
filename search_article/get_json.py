import os, sys
import json

from django.db import DatabaseError

# Добавление настроек в django для использования его в скриптах
proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'search_article.settings'

import django

django.setup()
from articles.models import Article, Category


# Получение значения из json
def get_data(line):
    create_timestamp = line['create_timestamp']
    timestamp = line['timestamp']
    language = line['language']
    wiki = line['wiki']
    category = line['category']
    title = line['title']
    auxiliary_text = line['auxiliary_text']
    return {'create_timestamp': create_timestamp, 'timestamp': timestamp,
            'language': language, 'wiki': wiki,
            'category': category, 'title': title, 'auxiliary_text': auxiliary_text}


# Прохожение циклом по папке с файлами и получением списка словарей
def get_list_data():
    list_data = []
    for filename in os.listdir('archive_data'):
        with open(os.path.join('archive_data', filename), 'r', encoding='utf-8') as file:
            data = [json.loads(line) for line in file]
            for line in data:
                try:
                    dict_data = get_data(line)
                    list_data.append(dict_data)
                except:
                    continue
    return list_data


# Сохранение в БД категорий и статей
def save_categories(list_data):
    for dict_data in list_data:
        categories = dict_data.pop('category', '')
        if categories:
            for category in categories:
                cat = Category(title=category)
                try:
                    cat.save()
                except DatabaseError:
                    pass
                qs = Category.objects.get(title=category)
                art = Article.objects.create(**dict_data)
                art.category.add(qs)
        else:
            try:
                Article.objects.create(**dict_data)
            except DatabaseError:
                pass


if __name__ == '__main__':
    list_data = get_list_data()
    save_categories(list_data)
