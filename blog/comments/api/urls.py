from django.conf.urls import include, url

from .views import(
    PostCommentCreateAPIView,
)


urlpatterns = [
    url(r'^post/create/$', PostCommentCreateAPIView.as_view(), name='post-comment-create'),
#    url(r'^(?P<slug>[\w-]+)/delete/$',
 #       CommentDestroyAPIView.as_view(), name='delete'),
]
