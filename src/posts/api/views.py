from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView
    )

from posts.models import Post
from .serializers import PostDetailSerializer, PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    #def get_queryset()



