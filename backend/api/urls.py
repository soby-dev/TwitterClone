from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='api-home'),
    path('tweet-list/', views.tweetList, name='tweet-list'),
    path('tweet-detail/<str:pk>/', views.tweetDetail, name='tweet-detail'),
    path('tweet-create/', views.tweetCreate, name='tweet-create')
]
