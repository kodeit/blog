from django.conf.urls import include, url

from .views import(
    PostCreateAPIView,
    PostListAPIView,
    PostDetailAPIView,
)


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name="list-api"),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create-api'),
    url(r'^(?P<slug>[-\w]+)/$',
        PostDetailAPIView.as_view(), name='detail-api'),
    #  url(r'^(?P<slug>[\w-]+)/edit/$',
    #    PostUpdateView.as_view(), name='post-update'),
    #  url(r'^(?P<slug>[\w-]+)/delete/$',
    #    PostDeleteView.as_view(), name='post_delete'),
]
