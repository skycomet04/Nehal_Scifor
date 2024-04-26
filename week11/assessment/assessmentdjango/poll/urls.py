from django.contrib import admin
from django.urls import path
from poll import views

urlpatterns = [
    path('',views.home,name='home'),
    path('createpoll',views.createpoll,name='createpoll'),
    path('result/<int:pid>',views.result,name='result'),
    path('vote/<int:pid>',views.vote,name='vote'),
]
