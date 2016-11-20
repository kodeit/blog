from django.conf.urls import include, url

from .views import (PostListView, PostDetailView, PostCreateView,)


urlpatterns = [
    url(r'^$', PostListView.as_view(), name="post-list"),
    url(r'^create/$', PostCreateView.as_view(), name='post-create'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post-detail'),
]
