from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('profile/', views.profile, name='profile'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('reading/<str:id>/', views.reading, name='reading'),
    path('adding/<str:id>/', views.adding, name='adding'),
    path('delete_relationship/<str:pk>/', views.delete, name='delete'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add/', views.add_book, name='add'),
    path('delete_book/<str:id>/', views.delete_book, name='delete_book'),
    path('update-user/', views.update_user, name='update-user'),
    path('delete_comment/<str:id>/', views.delete_comment, name='delete_comment')
]