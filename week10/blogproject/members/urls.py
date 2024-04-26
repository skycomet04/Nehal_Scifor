from django.contrib import admin
from django.urls import path
from .views import Userregisterview
urlpatterns = [
    path('register/',Userregisterview.as_view(),name='register'),
]
