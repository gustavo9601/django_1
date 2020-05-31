from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenido(request):
    return HttpResponse("Hello World from Django")

def despedirce(request):
    return HttpResponse("Say Good Bye Django")
