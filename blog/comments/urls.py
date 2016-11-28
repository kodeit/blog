from django.conf.urls import url

from .views import (CommentCreateView, CommentDeleteView)

urlpatterns = [
    url(r'^create/$', CommentCreateView.as_view(), name='comment-create'),
    url(r'^delete/(?P<pk>[-\w]+)$',
        CommentDeleteView.as_view(), name='comment-delete'),
]

