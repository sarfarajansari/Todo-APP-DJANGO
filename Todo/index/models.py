from django.db import models

# Create your models here.



class User(models.Model):
    name=models.CharField(default="",max_length=64,blank=True)

class Task(models.Model):
    task=models.CharField(max_length=500)
    done=models.BooleanField(default=False)
    start_date=models.DateField()
    complete_date=models.DateField(blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="tasks")

