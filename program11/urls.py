from django.urls import path
from .views import register_student,registration_page,insertcourse

urlpatterns = [
    path('course',insertcourse),
    path('register/',registration_page, name='registration_page'),
    path('register_student/',register_student, name='register_student'),
]
