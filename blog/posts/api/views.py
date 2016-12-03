from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)

from posts.models import Post

from .serializers import (
    PostCreateSerializer,
    PostDetailSerializer,
    PostListSerializer,
)


class PostCreateAPIView(CreateAPIView):

    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDestroyAPIView(RetrieveDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'slug'


class PostListAPIView(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostUpdateAPIView(RetrieveUpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
