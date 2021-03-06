from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Main.as_view()),
    path('login/', views.Login.as_view()),
    path('register/', views.Registration.as_view()),
    path('logout/', views.Logout.as_view()),
]

