from django import forms
from django.forms import ModelForm
from .models import Task

class TaskFormView(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add one task.....'}))

    class Meta:
        model=Task
        fields='__all__'
