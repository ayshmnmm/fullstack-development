from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def cdt(req):
    res = f"The time is {datetime.datetime.now()}"
    return HttpResponse(res)