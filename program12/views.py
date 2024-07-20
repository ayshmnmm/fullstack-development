from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def courselist(request):
    if request.method == 'POST':
        usn=request.POST['usn']
        try:
            obj=Student.objects.get(usn=usn)
            ans=''
            l=obj.courses.all().values()
            for x in l:
                ans=ans+x['cname']+'<br>'
            return HttpResponse(ans)
        except Exception:
            return HttpResponse('STUDENT USN DOENT EXIST/INVALID')
    else:
        return HttpResponse("method is not post")


def course_page(request):
    return render(request, 'course.html')