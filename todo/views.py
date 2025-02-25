from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def addTask(request):
    add_task = request.POST['task']
    Task.objects.create(task = add_task)
    return redirect('home')