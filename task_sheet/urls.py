from django.urls import path

from task_sheet.views import TaskIndexView, TaskCreateView, TaskDetailView, TaskDeleteView

urlpatterns = [
    path('', TaskIndexView.as_view(), name="index"),
    path('<int:pk>/', TaskDetailView.as_view(), name="task"),
    path('create/', TaskCreateView.as_view(), name="task_create"),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name="task_delete"),
]
