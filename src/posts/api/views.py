from rest_framework.generics import ListAPIView

from posts.models import Post

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()


