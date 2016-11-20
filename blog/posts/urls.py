from django.conf.urls import include, url

from .views import (PostListView, PostDetailView,
                    PostCreateView, PostUpdateView, PostDeleteView)


urlpatterns = [
    url(r'^$', PostListView.as_view(), name="post-list"),
    url(r'^create/$', PostCreateView.as_view(), name='post-create'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$',
        PostUpdateView.as_view(), name='post-update'),
    url(r'^(?P<slug>[\w-]+)/delete/$',
        PostDeleteView.as_view(), name='post_delete'),
]
