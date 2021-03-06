from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)

from posts.models import Category, Post
from .permissions import IsOwner

from .serializers import (
    CreateCategorySerializer,
    CategoryListSerializer,
    PostCreateSerializer,
    PostDetailSerializer,
    PostListSerializer,
)


class CategoryListAPIView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryCreateAPIView(CreateAPIView):

    serializer_class = CreateCategorySerializer
    permission_classes = (IsAuthenticated, )


class PostCreateAPIView(CreateAPIView):

    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDestroyAPIView(RetrieveDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsOwner, )
    lookup_field = 'slug'


class PostListAPIView(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('description', 'summary', 'title')
    ordering_fields = ('visit_count', 'created')


class PostUpdateAPIView(RetrieveUpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsOwner, )
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
