from django.urls import path
from . import views

urlpatterns = [
    path('dt/<int:n>', views.cdtn, name='p2'),
]
