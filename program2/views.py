from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def cdtn(req, n):
    res = f"The time after {n} hours will be {datetime.datetime.now() + datetime.timedelta(hours=n)}"
    res += f"<br />The time {n} hours ago was {datetime.datetime.now() - datetime.timedelta(hours=n)}"
    return HttpResponse(res)
