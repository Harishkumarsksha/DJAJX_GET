from django.urls import path
from myApp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('like/', views.like, name='like'),
]
