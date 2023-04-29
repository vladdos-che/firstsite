from django.urls import path
from hw2.views import index

urlpatterns = [
    path('', index),
]
