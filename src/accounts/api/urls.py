from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    )

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]
