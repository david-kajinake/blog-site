from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

tasks = [
    "Do this" , "Do that" , "Finish up" , "Repeat"
]

creators = [
    "David" , "Daniel" , "Denezel" , "Dominic"
]

task_creator_zipped =  list(zip(creators , tasks))
all_tasks = {}




class NewTaskForm(forms.Form):
    task_name = forms.CharField(label = "Enter a task name")
    task_giver = forms.CharField(label = "Enter a giver's name")




def view_tasks(request):

    return render( request , "tasks/view.html" , {
       "all_tasks": all_tasks
    } ) 

def add_tasks(request):
    if request.method == "POST":
        form = NewTaskForm()
        if form.is_valid():
            name_of_task = form.cleaned_data["task_name"]
            name_of_creator = form.cleaned_data["task_giver"]
            tasks.append(name_of_task)
            creators.append(name_of_creator)

            for task in task_creator_zipped:
                list(task)
                main_task = task[0]
                creator = task[1]
                overall = {
                    f"{main_task}": creator
                }
                all_tasks.update(overall)

        else:
            form_error_text = "One or all form inputs are invalid"
            return render(request , "tasks/add.html" , {
                "form": NewTaskForm() ,
                "form_error_text": form_error_text ,
            } )

    return render( request , "tasks/add.html" , {
        "form": NewTaskForm()
    } )
