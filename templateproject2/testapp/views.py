from django.shortcuts import render
import datetime

# Create your views here.
def wish_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = 'Hello guest !!! very good '

    if(h<12):
        msg = msg + 'morning !!!'
    elif(h<16):
        msg = msg + 'afternoong !!!'
    elif(h<21):
        msg = msg + 'evening !!!'
    else:
        msg = msg + 'night !!!'

    response = render(request,'testapp/results.html',{'m':msg,'date':date})

    return response
