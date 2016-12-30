from django.conf.urls import url

from rest_framework.authtoken.views import obtain_auth_token

from .views import (UserCreateAPIView)

urlpatterns = [
    url(r'^get_token', obtain_auth_token, name='get-token'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]