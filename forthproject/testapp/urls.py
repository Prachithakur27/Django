#from django.contrib import admin
from django.conf.urls import url
#from django.urls import path
from testapp import views

urlpatterns = [

    url('first/', views.first_view),
    url('second/', views.second_view),
    url('third/', views.third_view),
    url('forth/', views.forth_view),
    url('fifth/', views.fifth_view),
]
