from django.urls import path
from . import views

urlpatterns = [
    path('contactuswforms',views.contact_us)
]
