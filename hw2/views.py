from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from json_my_hw import MyJsonFile


def index(request):
    template = loader.get_template('index.html')
    f = MyJsonFile
    context = {'f': f}
    # return HttpResponse(f'JSON: {MyJsonFile.f}') Это я сделал для практического задания
    return HttpResponse(template.render(context))
