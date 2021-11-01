from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='api-home'),
    path('tweet-list/', views.tweetList, name='tweet-list'),
    path('tweet-detail/<str:pk>/', views.tweetDetail, name='tweet-detail'),
    path('tweet-create/', views.tweetCreate, name='tweet-create'),
    path('tweet-like/<str:pk>/', views.tweetLike, name='tweet-like'),
    path('tweet-delete/<str:pk>/', views.tweetDelete, name='tweet-delete')
]
