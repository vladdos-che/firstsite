from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from testapp.forms import SMSCreateForm
from testapp.models import SMS


def index_sms(request):
    template = get_template('testapp/index.html')
    return HttpResponse(template.render(request=request))


class AddSms(CreateView):
    template_name = 'testapp/create.html'
    form_class = SMSCreateForm
    success_url = reverse_lazy('index_sms')


class ReadSms(DetailView):
    model = SMS
    template_name = 'testapp/read.html'


class ReadListSms(ListView):
    model = SMS
    template_name = 'testapp/read.html'


class DeleteSms(DeleteView):
    model = SMS
    success_url = reverse_lazy('index_sms')


class UpdateSms(UpdateView):
    template_name = 'testapp/create.html'
    form_class = SMSCreateForm
    success_url = reverse_lazy('index_sms')
