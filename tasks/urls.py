from django.urls import path
from .views import (
    index,
    TaskTypeListView,
    PositionListView,
    WorkerListView,
    TaskListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list",
    ),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list",
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
]

app_name = "tasks"
