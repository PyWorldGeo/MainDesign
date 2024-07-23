from django.contrib import admin

# Register your models here.
from .models import Book, User, Author, Genre, Video
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Video, MyModelAdmin)
