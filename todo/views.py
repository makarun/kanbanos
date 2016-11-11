from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Task, Stage
from .forms import TaskForm, StageForm
from django.contrib.auth.decorators import login_required


def task_list(request):
    tasks = Task.objects.order_by('priority')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def task_add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.date = timezone.now()
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_add.html', {'form': form})    

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.date = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_add.html', {'form': form})

@login_required
def task_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def task_todo_list(request):
    tasks = Task.objects.order_by('priority')
    return render(request, 'todo/task_todo_list.html', {'tasks': tasks}) 

def task_doing_list(request):
    tasks = Task.objects.order_by('priority')
    return render(request, 'todo/task_doing_list.html', {'tasks': tasks})

def task_done_list(request):
    tasks = Task.objects.order_by('priority')
    return render(request, 'todo/task_done_list.html', {'tasks': tasks})

def task_aborted_list(request):
    tasks = Task.objects.order_by('priority')
    return render(request, 'todo/task_aborted_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_detail.html', {'task': task})

def add_stage_to_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = StageForm(request.POST)
        if form.is_valid():
            stage = form.save(commit=False)
            stage.task = task
            stage.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = StageForm()
    return render(request, 'todo/add_stage_to_task.html', {'form': form})

@login_required
def stage_remove(request, pk):
    stage = get_object_or_404(Stage, pk=pk)
    task_pk = stage.task.pk
    stage.delete()
    return redirect('task_detail', pk=task_pk)

@login_required
def change_achieved(request, pk):
    stage = get_object_or_404(Stage, pk=pk)
    stage.change_achieved()
    return redirect('task_detail', pk=stage.task.pk)
