# Develop a Model form for student that contains his topic chosen for project, languages used and
# duration with a model called project.

from django import forms
from .models import  Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

