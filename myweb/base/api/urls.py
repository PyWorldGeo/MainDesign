from django.urls import path
from . import views



urlpatterns = [
    path('', views.get_rotes),
    path('books/', views.get_books),
    path('books/<str:pk>', views.get_book)
]
