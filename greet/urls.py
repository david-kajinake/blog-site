from django.urls import path
from . import views

urlpatterns = [
    path("isyeartwentytwentyfive/", views.isyeartwentytwentyfive , name = "index" ) ,
    path("<str:name>/" , views.greet , name = "greet") ,
]