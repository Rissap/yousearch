from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Main.as_view()),
    path('search/', include("search.urls")),
]
