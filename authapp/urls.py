from django.urls import path

from authapp.views import login, logout, register, PasswordChangeRedirectView

app_name = "authapp"

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('change_password/', PasswordChangeRedirectView.as_view(), name='change_password'),  # lesson_39_hw
]
