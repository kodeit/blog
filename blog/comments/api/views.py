from django.contrib.contenttypes.models import ContentType

from rest_framework.generics import CreateAPIView

from .serializers import create_comment_serializer


class PostCommentCreateAPIView(CreateAPIView):

    def get_serializer_class(self):

        serializer_class = create_comment_serializer(
                    app_name = 'posts',
                    model = 'post',
                    user = self.request.user
                )

        return serializer_class
