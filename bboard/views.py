from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Здесь будет список объединений</h1>")
