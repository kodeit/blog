from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostDetailSerializer(ModelSerializer):

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
        ]


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'slug',
            'author',
            'title',
            'created',
            'summary',
        ]
