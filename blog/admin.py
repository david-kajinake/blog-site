from django.contrib import admin
from . models import Author ,  Post , Comment , Reply , Like ,  About 

# Register your models here.
admin.site.register([
    Author , 
    Post , 
    Comment , 
    Reply , 
    Like , 
    About
])