from django.contrib.contenttypes.models import ContentType

from rest_framework.serializers import ModelSerializer, IntegerField

from accounts.api.serializers import UserSerializer
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = [
            'user',
            'comment',
        ]


def create_comment_serializer(app_name, model, user):
    class CommentCreateSerializer(ModelSerializer):

        object_id = IntegerField(required=True)
        class Meta:
            model = Comment
            fields = [
                'comment',
                'object_id',
            ]

        def __init__(self, *args, **kwargs):
            self.app_name = app_name
            self.model = model
            super(CommentCreateSerializer, self).__init__(*args, **kwargs)


        def create(self, validated_data):

            app_name = self.app_name
            model = self.model
            object_id = validated_data.get("object_id")
            comment = validated_data.get("comment")

            instance = Comment()
            instance.user = user
            instance.comment = comment

            try:
                content_type = ContentType.objects.get(
                    app_label=app_name,
                    model=model)

                model_obj = content_type.get_object_for_this_type(id=object_id)
                instance.content_type = content_type
                instance.object_id = object_id
                instance.content_object = model_obj
            except:
                pass;

            instance.save()
            return instance

    return CommentCreateSerializer


class CommentDestroySerializer(ModelSerializer):

    class Meta:
        model = Comment

