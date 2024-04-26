from django.contrib import admin
from django.urls import path
from blog.api.views import (blogCreateApiView,
                            blogListApiView,
                            blogDetailApiView,
                            blogUpdateApiView,
                            blogDeleteApiView)
urlpatterns = [
    path('/create',blogCreateApiView.as_view(), name='create'),
    path('',blogListApiView.as_view(), name='list'),
    path('<int:id>',blogDetailApiView.as_view(),name='detail'),
    path('/update/<int:id>',blogUpdateApiView.as_view(),name='update'),
    path('/delete/<int:id>',blogDeleteApiView.as_view(),name='delete')
    
    
]
