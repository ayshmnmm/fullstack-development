from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['usn', 'name', 'sem', 'courses']
        widgets = {
            'courses': forms.CheckboxSelectMultiple(),
        }
        