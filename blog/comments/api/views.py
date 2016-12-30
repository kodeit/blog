from rest_framework.generics import CreateAPIView, DestroyAPIView

from comments.models import Comment
from posts.api.permissions import IsOwner
from .serializers import create_comment_serializer, CommentDestroySerializer



class PostCommentCreateAPIView(CreateAPIView):

    def get_serializer_class(self):

        serializer_class = create_comment_serializer(
                    app_name = 'posts',
                    model = 'post',
                    user = self.request.user
                )

        return serializer_class


class PostCommentDestroyAPIView(DestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializer
    permission_classes = (IsOwner,)
    lookup_field = 'pk'
