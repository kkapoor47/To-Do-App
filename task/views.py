from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskFormView

def home(request):
    tasks=Task.objects.all()
    form=TaskFormView()

    if request.method == 'POST':
        form=TaskFormView(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')


    context={
        'tasks':tasks,
        'form':form
    }
    return render(request,'task/home.html',context)

def editTask(request,pk):
    tasks=Task.objects.get(id=pk)
    form=TaskFormView(instance=tasks)

    if request.method == 'POST':
        form=TaskFormView(request.POST, instance=tasks)
        if form.is_valid():
            form.save()

            return redirect('/')

    context={
        'tasks':tasks,
        'form':form
    }
    return render(request,'task/edit_task.html',context)

def deleteTask(request,pk):
    item=Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context={
        'item':item
    }
    return render(request,'task/delete.html',context)