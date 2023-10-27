from django.urls import path

from authapp.views import login, logout, register, PasswordChangeRedirectView, api_users, APIBbUsersDel, \
    APIRubricViewSet

from authapp.views import APIBbUsers

app_name = "authapp"

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('change_password/', PasswordChangeRedirectView.as_view(), name='change_password'),  # lesson_39_hw

    # path('api/v1/users/', api_users),  # lesson_49_hw
    path('api/v1/users/', APIBbUsers.as_view()),  # lesson_52_hw
    # path('api/v1/users/', APIRubricViewSet.as_view()),  # lesson_52_hw

    path('api/v1/users/<str:username>/', APIBbUsersDel.as_view()),  # lesson_52_hw
]
