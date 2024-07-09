from django.db import models

# Create your models here.
# Develop a Model form for student that contains his topic chosen for project, languages used and
# duration with a model called project.
class Student(models.Model):
    usn=models.CharField(max_length=10, primary_key=True)
    name=models.CharField(max_length=30)
    sem=models.IntegerField()

class Project(models.Model):
    topic=models.CharField(max_length=30)
    languages=models.CharField(max_length=30)
    duration=models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

