from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting_view(request):
    return HttpResponse('<h1>Hello friends good morning...!!! Have a nice day.</h1>')
