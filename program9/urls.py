from django.urls import path
from .views import StudentDetailView,StudentListView

urlpatterns = [
    path('student_list/', StudentListView.as_view()),
    path('student_detail/<int:pk>/', StudentDetailView.as_view()),
]
