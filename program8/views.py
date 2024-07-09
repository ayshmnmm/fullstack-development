from django.shortcuts import render
from .forms import ProjectForm
from django.http import HttpResponse

# Create your views here.

def insertproject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Record inserted successfully")
    form = ProjectForm()
    return render(request, 'insertproject.html', {'form': form})
    