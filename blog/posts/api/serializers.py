from rest_framework.serializers import ModelSerializer

from accounts.api.serializers import UserSerializer
from comments.api.serializers import CommentSerializer

from comments.models import Comment
from posts.models import Post, Category


class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
        ]

class CreateCategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
        ]

class PostDetailSerializer(ModelSerializer):

    author = UserSerializer()
    comments = CommentSerializer(many=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'summary',
            'category',
            'description',
            'image',
            'comments',
        ]


class PostListSerializer(ModelSerializer):

    author = UserSerializer()

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'slug',
            'title',
            'created',
            'summary',
        ]


class PostCreateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'summary',
            'description',
            'image',
            'category',
        ]
