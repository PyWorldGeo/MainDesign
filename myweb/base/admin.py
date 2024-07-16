from django.contrib import admin

# Register your models here.
from .models import Book, User, Author, Genre

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Genre)