from django.urls import path
from . import views

urlpatterns = [
    path('student',views.insertstudent),
    path('course',views.insertcourse),
    path('enroll/<str:s>/<str:c>',views.enrollment),
    path('display',views.display),
]
