from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from testapp.forms import SMSCreateForm, ImgForm
from testapp.models import SMS, Img

from django.db import transaction


def index_sms(request):
    template = get_template('testapp/index.html')
    return HttpResponse(template.render(request=request))


class AddSms(CreateView):
    template_name = 'testapp/create.html'
    form_class = SMSCreateForm
    success_url = reverse_lazy('index_sms')


def add(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImgForm()

    context = {'form': form}

    return render(request, 'testapp/add.html', context)


def edit(request, pk):
    img = Img.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES, instance=img)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImgForm(instance=img)

    context = {'form': form, 'img': img}

    return render(request, 'testapp/edit.html', context)


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


# @transaction.non_atomic_requests
# def my_view(request):
#     # В этом контроллере действует режим обработки транзакций по умолчанию
#     pass
#
#
# # @transaction.atomic
# def edit(request, pk):
#     # В этом контроллере будет действовать режим атомарных запросов
#     with transaction.atomic():
#         # Набор транзакций
#         pass
#     return redirect('index')


# def my_function():
#     transaction.set_autocommit(False)
#     try:
#         # Операция
#         pass
#     except Exception:
#         transaction.rollback()
#     else:
#         transaction.commit()
#     finally:
#         transaction.set_autocommit(True)
#
#
# def my_controller():
#     if form.is_valid():
#         try:
#             form.save()
#             transaction.commit()
#         except:
#             transaction.rollback()
#
#
# def commit_handler():
#     # Выполняем какие-либо действия после подтверждения транзакции
#     pass
#
#
# def my_controller():
#     if formset.is_valid():
#         for form in formset:
#             if form.cleaned_data:
#                 sp = transaction.savepoint()
#                 try:
#                     form.save()
#                     transaction.savepoint_commit(sp)
#                 except:
#                     transaction.savepoint_rollback(sp)
#                     transaction.commit()
#                 finally:
#                     transaction.on_commit(commit_handler)
