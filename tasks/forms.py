from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Task, TaskType, Position


class TaskTypeNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name",
                "class": "form-control bg-darker text-secondary border-darker"
            }
        ),
    )


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter task type name",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2 w-75"
                }
            ),
        }


class PositionNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name",
                "class": "form-control bg-darker text-secondary border-darker"
            }
        ),
    )


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter position name",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2 w-75"
                }
            ),
        }


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "position")

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Enter username",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter first name",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter last name",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
            "position": forms.Select(
                attrs={
                    "class": "form-select bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
        }

    # Додаємо стилізацію для password1 і password2
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "placeholder": "Enter password",
                "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "placeholder": "Confirm password",
                "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
            }
        )


class WorkerPositionUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "position")

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Enter username",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter first name",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter last name",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
            "position": forms.Select(
                attrs={
                    "class": "form-select bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
        }


class WorkerUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username",
                "class": "form-control bg-darker text-secondary border-darker"
            }
        ),
    )


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input me-2"
            }
        ),
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
            }
        ),
        input_formats=("%Y-%m-%dT%H:%M",),
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter task name",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter task description",
                    "class": "form-control bg-darker text-general border-darker rounded-3 px-3 py-2",
                    "rows": 4
                }
            ),
            "priority": forms.Select(
                attrs={
                    "class": "form-select bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
            "task_type": forms.Select(
                attrs={
                    "class": "form-select bg-darker text-general border-darker rounded-3 px-3 py-2"
                }
            ),
            "is_completed": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }


class TaskNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name",
                "class": "form-control bg-darker text-secondary border-darker"
            }
        ),
    )
