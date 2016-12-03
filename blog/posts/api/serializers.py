from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from posts.models import Post, Category
from comments.models import Comment

User = get_user_model()


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'user',
            'comment',
        ]


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
        ]


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
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
            'title',
            'summary',
            'description',
            'image',
            'category',

        ]
