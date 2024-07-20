from django.urls import path
from .views import course_page, courselist

urlpatterns = [
    path('course', course_page),
    path('courselist', courselist, name='courselist'),
]
