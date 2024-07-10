from django.urls import path
from . import views

urlpatterns = [
    path('generate_csv/', views.generate_csv, name='generate_csv'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
]
