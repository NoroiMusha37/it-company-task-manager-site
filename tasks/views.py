from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import TaskType, Position, Task, Worker
from .forms import WorkerCreationForm, TaskForm


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


class TaskTypeListView(generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"
    paginate_by = 2


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    template_name = "tasks/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-type-list")


class PositionListView(generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "tasks/position_list.html"
    paginate_by = 2


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:position-list")


class WorkerListView(generic.ListView):
    model = get_user_model()
    queryset = get_user_model().objects.prefetch_related("position")
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        position_id = self.request.GET.get("position")
        if position_id:
            queryset = queryset.filter(position_id=position_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        position_id = self.request.GET.get("position")
        if position_id:
            context["position"] = Position.objects.get(pk=position_id)
        return context


class WorkerDetailView(generic.DetailView):
    model = get_user_model()


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:worker-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"
    queryset = Task.objects.select_related("task_type")
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        task_type_id = self.request.GET.get("task_type")
        if task_type_id:
            queryset = queryset.filter(task_type_id=task_type_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_type_id = self.request.GET.get("task_type")
        if task_type_id:
            context["task_type"] = TaskType.objects.get(pk=task_type_id)
        return context


class TaskDetailView(generic.DetailView):
    model = Task
    queryset = Task.objects.prefetch_related("assignees")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")
