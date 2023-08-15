from django.forms import ModelForm
from task_sheet.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'content', 'do_before_date')
