from django.shortcuts import render
#from django.http import HttpResponse
import datetime

# Create your views here.
def template_view(request):
    dt = datetime.datetime.now()
    name = 'prachi'
    rollno = 18156
    marks = 100
    my_dict = {'date' : dt,'name':name, 'rollno': rollno,'marks':marks}

    return render(request,'testapp/result.html',context = my_dict)
