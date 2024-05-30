from django.urls import path
from . import views

urlpatterns = [
    path('listy', views.prog3func, name='p3'),
]
