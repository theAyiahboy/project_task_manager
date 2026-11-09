
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProjectForm, TaskForm
from .models import Project, Task 


def home(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(
            owner=request.user
        ).prefetch_related("tasks")
    else:
        projects = Project.objects.none()

    return render(request, "home.html", {
        "projects": projects
    })

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            return redirect("home")

    else:
        form = ProjectForm()

    return render(request, "create_project.html", {"form": form})

@login_required
def create_task(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id,
        owner=request.user
    )

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()

            return redirect("home")

    else:
        form = TaskForm()

    return render(request, "create_task.html", {
        "form": form,
        "project": project
    })

@login_required
def edit_project(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id,
        owner=request.user
    )

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = ProjectForm(instance=project)

    return render(request, "edit_project.html", {
        "form": form,
        "project": project
    })


@login_required
def delete_project(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id,
        owner=request.user
    )

    if request.method == "POST":
        project.delete()
        return redirect("home")

    return render(request, "delete_project.html", {
        "project": project
    })

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        project__owner=request.user
    )

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = TaskForm(instance=task)

    return render(request, "edit_task.html", {
        "form": form,
        "task": task
    })

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        project__owner=request.user
    )

    if request.method == "POST":
        task.delete()
        return redirect("home")

    return render(request, "delete_task.html", {
        "task": task
    })