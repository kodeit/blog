from django.conf.urls import include, url

from .views import(
    CategoryCreateAPIView,
    CategoryListAPIView,
    # Post API Classes
    PostCreateAPIView,
    PostDetailAPIView,
    PostDestroyAPIView,
    PostListAPIView,
    PostUpdateAPIView,
)


urlpatterns = [
    # Category URLs
    url(r'^category/list$',
        CategoryListAPIView.as_view(), name='category-list-api'),
    url(r'^category/create/$',
        CategoryCreateAPIView.as_view(), name='category-create-api'),

    url(r'^$', PostListAPIView.as_view(), name="list-api"),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create-api'),
    url(r'^(?P<slug>[-\w]+)/$',
        PostDetailAPIView.as_view(), name='detail-api'),
    url(r'^(?P<slug>[\w-]+)/edit/$',
        PostUpdateAPIView.as_view(), name='update-api'),
    url(r'^(?P<slug>[\w-]+)/delete/$',
        PostDestroyAPIView.as_view(), name='delete-api'),
]
