from django.shortcuts import render
from django.http import HttpResponse
import time

current = time.localtime()
print(current.tm_year)
# Create your views here.

def greet(request , name):
    return HttpResponse(f"Hello {name.capitalize()} How is it going today ??")

def isyeartwentytwentyfive(request):
    current_time = time.localtime()
    get_year = current_time.tm_year
    isyear_twenty_twenty_five = get_year == 2022
    return render( request, "greet/index.html",{
        "current_year": isyear_twenty_twenty_five ,
        "present_year": get_year ,
    } ) 
