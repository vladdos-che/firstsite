from django.urls import path, re_path

from tasksheet.views import index, login, my_tasks, history, add_task, lesson_15_hw

urlpatterns = [
    path('', index, name='index'),
    # re_path(r'^$', index, name='index'),

    path('login/', login, name='login'),
    # re_path(r'^login/$', login, name='login'),

    path('my_tasks/', my_tasks, name='my_tasks'),
    # re_path(r'^my_tasks/$', my_tasks, name='my_tasks'),

    path('history/', history, name='history'),
    # re_path(r'^history/$', history, name='history'),

    path('add_task/', add_task, name='add_task'),
    # re_path(r'^add_task/$', add_task, name='add_task'),

    path('lesson_15_hw/', lesson_15_hw, name='lesson_15_hw'),
]
