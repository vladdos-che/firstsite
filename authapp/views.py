from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.views.generic import ListView, FormView, TemplateView
from django.urls import reverse_lazy

from authapp.forms import UserLoginForm, UserViewForm, RegisterUserForm
from authapp.models import MyUser


def login(request):
    title = "Login"
    login_form = UserLoginForm(data=request.POST)

    if request.method == "POST" and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
    }

    return render(request, 'authapp/login.html', context)


def register(request):
    title = "регистрация"

    if request.method == 'POST':
        register_form = RegisterUserForm(data=request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = RegisterUserForm()

    context = {
        'title': title,
        'register_form': register_form,
    }

    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


# def user_view(request):
#     title = "UserSearch"
#
#     if request.method == "POST":
#         user_form = UserViewForm(data=request.POST)
#         if user_form.is_valid():
#             # user = request.users[request.POST['user_name']]
#             user = request.users[request.POST['user_name']]
#
#             context = {
#                 'user_form': user_form,
#                 'user': user,
#                 'title': title,
#             }
#
#             return render(request, 'authapp/userview.html', context)
#
#     else:
#         user_form = UserViewForm()
#
#     context = {
#         'user_form': user_form,
#         'title': title,
#     }
#     return render(request, 'authapp/userview.html', context)


class UserByNameView(FormView):  # lesson_19_hw
    template_name = 'authapp/userview.html'
    form_class = UserViewForm
    success_url = '/auth/user/'
    title = "UserSearch"

    user_form = None
    my_user = None

    def form_valid(self, form):
        if self.request.method == "POST":
            self.user_form = UserViewForm(data=self.request.POST)
            if self.user_form.is_valid():
                data = self.user_form.cleaned_data.get("user_name")
                self.my_user = MyUser.objects.get(name=data)
        else:
            self.user_form = UserViewForm()
        self.get_context_data()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        print(self.user_form)
        print(self.my_user)

        context = super().get_context_data(**kwargs)

        context['my_user'] = self.my_user
        context['user_form'] = self.user_form

        return context


class UserListView(ListView):  # lesson_19_hw
    template_name = 'authapp/userview.html'
    title = "UsersList"
    context_object_name = 'my_users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return MyUser.objects.all()
