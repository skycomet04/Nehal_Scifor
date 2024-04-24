from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=350)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name

def get_current_user():
    return get_user_model().objects.get(username='nehal').id
class Blog(models.Model):
    title=models.CharField(max_length=120)
    image=models.FileField(upload_to='media/',null=True,blank=True)
    content=models.TextField()
    date=models.DateField(auto_now=False,auto_now_add=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,default=get_current_user)
    def __str__(self):
        return self.title
def getblogid():
    return Blog.objects.get(title="Calculator").id   
class Comment(models.Model):
    blog=models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE,default=getblogid)
    author=models.CharField(max_length=155)
    comment_desc=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.author