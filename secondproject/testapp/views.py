from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_morning_view(request):
    return HttpResponse('<h1> Hello good morning friends </h1>')

def good_evening_view(request):
    return HttpResponse('<h1> Hello good evening friends </h1>')

def good_night_view(request):
    return HttpResponse('<h1> Hello good night friends </h1>')
