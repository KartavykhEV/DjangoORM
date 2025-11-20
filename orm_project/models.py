from django.db import models

# Авторы книг
class Author(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    alive = models.BooleanField()

# категия книг
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)

# книга
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    release_date = models.DateField()

# связь книга - категория
class BookCategory(models.Model):
    pk = models.CompositePrimaryKey("book", "category")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        unique_together = ['book', 'category']  # Уникальная комбинация потому, что Django ORM НЕ умеет делать композитные ключи

