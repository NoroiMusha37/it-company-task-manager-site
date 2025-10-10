from django.urls import path
from .views import (
    index,
    TaskTypeListView,
    PositionListView,
    WorkerListView,
    TaskListView,
    WorkerDetailView,
    TaskDetailView,
    TaskTypeCreateView,
    PositionCreateView,
    WorkerCreateView,
    TaskCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list",
    ),
    path(
        "task-types/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create"
    ),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list",
    ),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create"
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
]

app_name = "tasks"
