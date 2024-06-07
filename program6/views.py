from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Student,Course
def insertstudent(request):
    s1=Student(usn='21CS001', name='ABITH', sem=6)
    s2=Student(usn='21CS002', name='RAM', sem=6)
    s3=Student(usn='21CS003', name='SAM', sem=6)
    s4=Student(usn='21CS004', name='KUMAR', sem=6)
    s5=Student(usn='21CS005', name='RAJ', sem=6)
    for x in [s1,s2,s3,s4,s5]:
        x.save()
    return HttpResponse("insertion of student data successful")

def insertcourse(request):
    c1=Course(cid='21CS61',cname='SEPM')
    c2=Course(cid='21CS62',cname='FD')
    c3=Course(cid='21CS63',cname='CG')
    c4=Course(cid='21CS641',cname='AJJ')
    c5=Course(cid='21CS642',cname='DSV')
    for x in [c1,c2,c3,c4,c5]:
        x.save()
    return HttpResponse("insertion of course data successful") 

def enrollment(request,s,c):
    s=Student.objects.get(usn=s)
    l=c.split(',')
    for x in l:
        cc=Course.objects.get(cname=x)
        s.courses.add(cc)
    return HttpResponse("course enrollment successful") 

def display(request):
    s=Student.objects.all()
    res="<table border='2'><tr><th>USN</th><th>   NAME </th> <th> SEM </th><th>   COURSES</th></tr>"
    for x in s:
        res+="<tr><td>"+x.usn+"</td><td>"+x.name+"</td><td> "+str(x.sem)+"</td><td>  "
        l=x.courses.all().values()
        for a in l:
            res+=a['cname']+" , "
        res+="</td></tr>"
    res+="</table>"
    return HttpResponse(res)