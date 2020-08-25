from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def home_page_view(request):
    #students = Student.objects.all()
    #students = Student.objects.filter(marks_Lt = 35)
    #students = Student.objects.filter(name_startswith='A')
    students = Student.objects.all().order_by('marks')

    return render(request,'testapp/index.html',{'students':students})
