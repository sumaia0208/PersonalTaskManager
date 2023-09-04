from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task


def tasks(request):
    # only authenticate & logged in user see own tasks.
    if request.user.is_authenticated:
        # only retrieve logged in user's Tasks
        tasks = Task.objects.filter(user=request.user)
        return render(request, "list_tasks.html", {"tasks": tasks})
    else:
        return redirect("login")


# for creating task
def create_task(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST.get("title")
            status = "P" if request.POST.get("status") is None else request.POST.get("status")
            description = request.POST.get("description")
            due_date = request.POST.get("due_date")
            task = Task(
                user=request.user,
                title=title,
                status=status,
                description=description,
                due_date=due_date
            )
            task.save()
            return redirect("task_home")
    else:
        return redirect("login")
    return render(request, "create_task.html")


def update_task(request, pk):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=pk)
        if request.method == "POST":
            title = request.POST.get("title")
            status = "P" if request.POST.get("status") is None else request.POST.get("status")
            description = request.POST.get("description")
            due_date = request.POST.get("due_date")
            task.title = title
            task.status = status
            task.description = description
            task.due_date = due_date
            task.save()
            return redirect("task_home")
        return render(request, "update_task.html", {"task": task})
    else:
        return redirect("login")


def task_detail(request, pk):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=pk)
        return render(request, "details.html", {"task": task})
    else:
        return redirect("login")


def delete_task(request, pk):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=pk)
        task.delete()
        messages.success(request, 'Task successfully deleted!')
        return redirect("task_home")
    else:
        return redirect("login")
