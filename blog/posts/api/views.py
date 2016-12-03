from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from posts.models import Post
from .serializers import (
    PostCreateSerializer,
    PostDetailSerializer,
    PostListSerializer,
)


class PostDetailAPIView(RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostListAPIView(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostCreateAPIView(CreateAPIView):

    serializer_class = PostCreateSerializer
