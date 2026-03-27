from django.urls import path
from . import views

# Tasks views

urlpatterns = [
    path("view/" , views.view_tasks , name ="view_tasks") ,
    path("add/" , views.add_tasks , name = "add_tasks")
]
 