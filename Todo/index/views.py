from django.shortcuts import render,redirect
from .models import*
import datetime

# Create your views here.

def index(request):
    if request.method=="GET":
        if "id" in request.session:
            if request.session["id"] in User.objects.values_list('id',flat=True):
                user=User.objects.get(pk=request.session["id"]) 
            else:
                user=User()
                user.save()
                request.session["id"]=user.id

        else:
            user=User()
            user.save()
            request.session["id"]=user.id
        
        tasks=user.tasks.all()
        return render(request,"index.html",{
            "tasks":tasks
        })
    else:
        if "task" in request.POST:
            if "id" in request.session:
                if request.session["id"] in User.objects.values_list('id',flat=True):
                    user=User.objects.get(pk=request.session["id"]) 
                else:
                    user=User()
                    user.save()
                    request.session["id"]=user.id

            else:
                user=User()
                user.save()
                request.session["id"]=user.id
                
            today=datetime.datetime.now()
            
            task=Task(task=request.POST["task"],user=user,start_date=today.date())
            task.save()
            return redirect("/")


def delete_task(request):
    if request.method=="POST":
        if "rmtask" in request.POST:
            task_id= int(request.POST["rmtask"])
            if task_id in Task.objects.values_list("id",flat=True):
                today=datetime.datetime.now()
                task=Task.objects.get(pk=task_id)
                task.complete_date=today.date()
                task.done=True
                task.save()


    return redirect("/")



def completed(request):
    if "id" in request.session:
        user=User.objects.get(pk=request.session["id"]) 
        tasks=user.tasks.all()
        return render(request,"history.html",{
            "tasks":tasks
        })

    redirect("/")
        
        
            


        




