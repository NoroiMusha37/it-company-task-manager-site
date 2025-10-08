from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tasks.models import TaskType, Position, Task


@login_required
def index(request):
    """View function for the home page of the site."""

    num_task_types = TaskType.objects.all().count()
    num_positions = Position.objects.all().count()
    num_workers = get_user_model().objects.all().count()
    num_tasks = Task.objects.all().count()

    context = {
        "num_task_types": num_task_types,
        "num_positions": num_positions,
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }

    return render(request, "tasks/index.html", context=context)
