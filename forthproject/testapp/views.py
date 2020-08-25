from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse('<h1>Response from 1st view </h1>')

def second_view(request):
    return HttpResponse('<h1>Response from 2nd view </h1>')

def third_view(request):
    return HttpResponse('<h1>Response from 3rd view </h1>')

def forth_view(request):
    return HttpResponse('<h1>Response from 4th view </h1>')

def fifth_view(request):
    return HttpResponse('<h1>Response from 5th view </h1>')
