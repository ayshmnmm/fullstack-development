from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^mode/(?P<n>[0-9,]+[0-9])$', views.mode),
]
