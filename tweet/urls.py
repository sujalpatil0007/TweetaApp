from django.urls import path
from . import views

urlpatterns = [

    # 🔹 Home / Tweet List + Search
    path('', views.tweet_list, name='tweet_list'),

    # 🔹 Create Tweet
    path('create/', views.tweet_create, name='tweet_create'),

    # 🔹 Edit Tweet
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),

    # 🔹 Delete Tweet
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),

    # 🔹 Register User
    path('register/', views.register, name='register'),
]