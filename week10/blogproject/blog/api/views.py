from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView)
from blog.models import Blog
from .serializers import PostSerializer,PostDetailSerializer,PostCreateSerializer

class blogCreateApiView(CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=PostCreateSerializer
class blogListApiView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=PostSerializer
class blogDetailApiView(RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class=PostDetailSerializer
    lookup_field='id'
class blogDeleteApiView(DestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=PostDetailSerializer
    lookup_field='id'
class blogUpdateApiView(UpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class=PostDetailSerializer
    lookup_field='id'