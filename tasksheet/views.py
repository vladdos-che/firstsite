from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    pass


def login(request):
    pass


def my_tasks(request):
    pass


def history(request):
    pass


def add_task(request):
    pass


def lesson_15_hw(request):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
               "fox", "ant", "bird", "lion", "wolf", "deer",
               "bear", "frog", "hen", "mole", "duck", "goat"]
    # data = [animals[i] for i in range(len(animals))]  # Я знаю, что это бред и безсмысленно, но я умею
    data = {}
    for i in range(len(animals)):
        data.update({i: animals[i]})

    return JsonResponse(data, safe=False)
