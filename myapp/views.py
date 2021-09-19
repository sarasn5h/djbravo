from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def removepunc(request):
    return HttpResponse("<h1> home  </h1>")


def cap(request):
    return HttpResponse("i am cap")
