from rest_framework import serializers
from blog.models import Blog 

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['title','content','updated','date']
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['id','title','content','updated']
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['id','title','content','updated',"date"]
