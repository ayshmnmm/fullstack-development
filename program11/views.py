from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .forms import StudentForm
from .models import Course

# Create your views here.


def insertcourse(request):
    c1=Course(cid='21CS61',cname='SEPM')
    c2=Course(cid='21CS62',cname='FD')
    c3=Course(cid='21CS63',cname='CG')
    c4=Course(cid='21CS641',cname='AJJ')
    c5=Course(cid='21CS642',cname='DSV')
    for x in [c1,c2,c3,c4,c5]:
        x.save()
    return HttpResponse("insertion of course data successful")

def registration_page(request):
    form = StudentForm()
    return render(request, 'student.html', {'form': form})

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request'})
