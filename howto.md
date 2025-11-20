1. pip install django
2. cd ...
3. django-admin startproject myproject .
4. pip install psycopg2-binary
5. настроить подключение к БД
6. python manage.py makemigrations			# создать миграции
7. python manage.py migrate				# применить миграции
8. python manage.py showmigrations			# показать все миграции
9. создать модель в файле models.py
10. убедиться, что приложение прописано в списке INSTALLED\_APPS
11. python manage.py makemigrations orm\_project		# создать миграцию для указанного приложения

Добавляем API
1. pip install djangorestframework

