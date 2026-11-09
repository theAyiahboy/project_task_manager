
from django import forms
from .models import Project
from .models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200',
                'placeholder': 'Enter your project name',
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200',
                'placeholder': 'Describe your project...',
                'rows': 4,
            }),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'priority',
            'status',
            'due_date',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200',
                'placeholder': 'Enter task title',
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200',
                'placeholder': 'Describe the task...',
                'rows': 4,
            }),

            'priority': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200',
            }),

            'status': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200',
            }),

            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200',
            }),
        }