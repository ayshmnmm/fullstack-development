from django.urls import path
from . import views

urlpatterns = [
    path('studenta',views.home),
]