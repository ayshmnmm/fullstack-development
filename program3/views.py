from django.shortcuts import render

# Create your views here.
def prog3func(request):
    context = {
        'fruits' : ['Apple','Banana','Cherry'],
        'students' : ['Ram','Sam','Tam','Zam']
    }

    return render(request,'listy.html',context)
