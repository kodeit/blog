from django.conf.urls import include, url

from .views import(
    PostCommentCreateAPIView,
    PostCommentDestroyAPIView,
)


urlpatterns = [
    url(r'^post/create/$', PostCommentCreateAPIView.as_view(),
        name='post-comment-create'),
    url(r'^post/(?P<pk>[\d]+)/delete/$', PostCommentDestroyAPIView.as_view(),
        name='post-comment-delete'),
]
