import os.path
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail

from django.db import transaction
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView,\
    DeleteView, UpdateView

from firstsite.settings import BASE_DIR
from testapp.forms import ImgForm
from testapp.models import Img

FILES_ROOT = os.path.join(BASE_DIR, 'files')


# def index_sms(request):
#     template = get_template('testapp/index.html')
#     return HttpResponse(template.render(request=request))


def add(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['img']
            fn = '%s%s' % (datetime.now().timestamp(),
                           os.path.splitext(uploaded_file.name)[1])
            fn = os.path.join(FILES_ROOT, fn)

            with open(fn, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return redirect('testapp:index')
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
            # return redirect('index')
            messages.add_message(request, messages.SUCCESS, 'Картинка изменена', extra_tags='first second')
            # messages.success(request, 'Картинка изменена', extra_tags='first second')

            msgs = messages.get_messages(request)
            first_message_text = msgs[0].message
            print(first_message_text)
    else:
        form = ImgForm(instance=img)

    context = {'form': form, 'img': img}

    return render(request, 'testapp/edit.html', context)


def index(request):
    imgs = []

    for entry in os.scandir(FILES_ROOT):
        imgs.append(os.path.basename(entry))
        print('FILE: ', os.path.basename(entry))
    print(imgs)
    context = {'imgs': imgs}
    return render(request, 'testapp/index.html', context)


def get(request, filename):
    fn = os.path.join(FILES_ROOT, filename)
    return FileResponse(open(fn, 'rb'), content_type='application/octet-stream')


# class AddSms(CreateView):
#     template_name = 'testapp/create.html'
#     form_class = SMSCreateForm
#     success_url = reverse_lazy('index_sms')


# class ReadSms(DetailView):
#     model = SMS
#     template_name = 'testapp/read.html'
#
#
# class ReadListSms(ListView):
#     model = SMS
#     template_name = 'testapp/read.html'
#
#
# class DeleteSms(DeleteView):
#     model = SMS
#     success_url = reverse_lazy('index_sms')
#
#
# class UpdateSms(UpdateView):
#     template_name = 'testapp/create.html'
#     form_class = SMSCreateForm
#     success_url = reverse_lazy('index_sms')


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


def test_cookie(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        print("COOKIES ARE DELETED!!!")
    else:
        print("USER, ON COOKIES!!!")
        # Веб-обозреватель не поддерживает cookie

    request.session.set_test_cookie()
    return render(request, 'testapp/test_cookie.html')


def test_mail(request):
    title = 'Test2'
    message = 'Test2!!!'
    em_from = 'webmaster@supersite.ru'
    em_to = ['user@othersite.ru']
    html_mes = '<h1>!!! TEXT2 !!!</h1>'

    send_mail(title, message, em_from, em_to, html_message=html_mes, fail_silently=False)

    return redirect('testapp:index')
