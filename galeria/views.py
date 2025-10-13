from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def index2(request):
    return HttpResponse("<h1>Alura Space-2</h1>")

def index3(request):
    return HttpResponse("<h1>Alura Space-3</h1>")
