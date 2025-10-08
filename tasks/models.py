from django.contrib.auth.models import User, AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    PRIORITIES = [
        ("P0", "Critical"),
        ("P1", "High"),
        ("P2", "Moderate"),
        ("P3", "Low"),
        ("P4", "Negligible"),
    ]
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITIES)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker)

    def __str__(self):
        return f"{self.name} ({self.priority}) {self.deadline}"
