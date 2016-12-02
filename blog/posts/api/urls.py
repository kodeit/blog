from django.conf.urls import include, url

from .views import (PostListAPIView, PostDetailAPIView)


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name="post-api-list"),
    url(r'^(?P<slug>[-\w]+)/$',
        PostDetailAPIView.as_view(), name='post-api-detail'),
    #  url(r'^create/$', PostCreateView.as_view(), name='post-create'),
    #  url(r'^(?P<slug>[\w-]+)/edit/$',
    #    PostUpdateView.as_view(), name='post-update'),
    #  url(r'^(?P<slug>[\w-]+)/delete/$',
    #    PostDeleteView.as_view(), name='post_delete'),
]
