from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.contrib import messages

from task_sheet.forms import TaskForm
from task_sheet.models import Task


class TaskIndexView(ListView):
    template_name = 'task_sheet/index.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.order_by('-published')
        return context


class TaskCreateView(CreateView):
    template_name = 'task_sheet/create.html'
    form_class = TaskForm
    success_url = '/'


class TaskDetailView(DetailView):
    template_name = "task_sheet/detail.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=self.kwargs['pk'])
        return context


class TaskDeleteView(DeleteView):
    template_name = "task_sheet/delete.html"
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')
