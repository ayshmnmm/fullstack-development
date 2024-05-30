from django.shortcuts import render
from .models import Student

# Create your views here.
def home(req):
    context = {
        'students': Student.objects.all().values(),
    }
    return render(req,'table.html',context)
