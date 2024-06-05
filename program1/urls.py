from django.urls import path
from . import views

urlpatterns = [
    path('dt', views.cdt, name='p1'),
]
