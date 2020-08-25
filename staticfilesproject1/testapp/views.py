from django.shortcuts import render
import datetime

# Create your views here.
def date_time_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    if(h<12):
        msg='Hello friends, Good Morning !!!'
    elif(h<16):
        msg = 'Hello friends, Good Afternoon !!!'
    elif(h<21):
        msg = 'Hello friends, Good Evening !!!'
    else:
        msg = 'Hello friends, Good Night !!!'

    my_dict = {'date':date,'msg':msg}

    return render(request,'testapp/results.html',my_dict)
