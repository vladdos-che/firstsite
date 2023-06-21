from django.urls import path, re_path

from tasksheet.views import index, login, my_tasks, history, add_task, lesson_15_hw

urlpatterns = [
    # path('sheets/', index, name='index'),
    # # re_path(r'^$', index, name='index'),
    #
    # path('sheets/login/', login, name='login'),
    # # re_path(r'^login/$', login, name='login'),
    #
    # path('sheets/my_tasks/', my_tasks, name='my_tasks'),
    # # re_path(r'^my_tasks/$', my_tasks, name='my_tasks'),
    #
    # path('sheets/history/', history, name='history'),
    # # re_path(r'^history/$', history, name='history'),
    #
    # path('sheets/add_task/', add_task, name='add_task'),
    # # re_path(r'^add_task/$', add_task, name='add_task'),
    #
    # path('sheets/lesson_15_hw/', lesson_15_hw, name='lesson_15_hw'),
]
