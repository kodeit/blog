from django.conf.urls import include, url

from .views import (PostListView)


urlpatterns = [
    url(r'^$', PostListView.as_view(), name="post-list"),
]
