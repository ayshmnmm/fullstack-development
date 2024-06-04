from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()

class Student(models.Model):
    USN = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    sem = models.IntegerField()
    course = models.ManyToManyField(Course)
    