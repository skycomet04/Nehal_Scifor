from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('blogs',views.blogs_list,name='blog_list'),
    path('blogs_detail/<int:id>',views.blogs_detail,name='blogs_detail'),
    path('createblog',views.createblog, name='createblog'),
    path('deleteblog/<int:id>', views.deleteblog, name="deleteblog"),
    path('updateblog/<int:id>',views.updateblog, name='updateblog'),
    path('blogs_detail/<int:bid>/createcomment',views.createcomment, name='createcomment'),
    path('contact',views.contact, name='contact'),
    path('practice',views.practice,name='practice')
]
