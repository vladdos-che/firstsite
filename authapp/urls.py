from django.urls import path

from authapp.views import login, logout, UserListView, UserByNameView

app_name = "authapp"

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('user/', UserByNameView.as_view(), name='user'),  # lesson_19_hw
    path('userlist/', UserListView.as_view(), name='user_list'),  # lesson_19_hw
]
