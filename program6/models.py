from django.db import models

# Create your models here.
class Course(models.Model):
    cid=models.CharField(max_length=10, primary_key=True)
    cname=models.CharField(max_length=30)

class Student(models.Model):
    usn=models.CharField(max_length=10, primary_key=True)
    name=models.CharField(max_length=30)
    sem=models.IntegerField()
    courses=models.ManyToManyField(Course)
