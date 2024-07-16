from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.exceptions import ValidationError


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Book(models.Model):
    creator = models.ForeignKey('User', on_delete=models.SET("Unknown User"))
    picture = models.ImageField(null=True, blank=True, default="no_cover.png")
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET("Unknown Author"))
    genre = models.ManyToManyField(Genre, related_name='books', blank=True)
    description = models.TextField(max_length=1000)
    file = models.FileField(null=True)

    updated = models.DateTimeField(auto_now=True)  # when updated
    created = models.DateTimeField(auto_now_add=True)  # when created

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f"{self.name} _ {self.author}"


class User(AbstractUser):
    books = models.ManyToManyField(Book, related_name='users', blank=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

class Animal(models.Model):
    name = models.CharField(max_length=200)
    sound = models.CharField(max_length=200)

    def speak(self):
        return f'The {self.name} says "{self.sound}"'

#py manage.py test
#py manage.py test --pattern="tests.py"
