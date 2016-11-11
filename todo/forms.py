from django import forms

from .models import Task, Stage

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'text', 'priority', 'category')

class StageForm(forms.ModelForm):
    
    class Meta:
        model = Stage
        fields = ('title', 'text', 'achieved')
    