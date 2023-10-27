from django.db import transaction
from django.dispatch import Signal
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.views.generic import ListView, FormView, TemplateView, RedirectView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from authapp.forms import UserLoginForm, RegisterUserForm
from authapp.models import BbUser
from authapp.serializers import BbUserSerializer
from authapp.signals import create_user_profile, user_logout


def login(request):
    title = "Login"
    login_form = UserLoginForm(data=request.POST)

    if request.method == "POST" and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)

            create_user_profile.send(sender=BbUser.objects.get(
                username=login_form.cleaned_data.get('username')
            ))  # lesson_42_hw

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

        if register_form.is_valid():  # lesson_31_hw
            transaction.set_autocommit(False)
            try:
                register_form.save()
            except:
                transaction.rollback()
            else:
                transaction.commit()
            finally:
                transaction.set_autocommit(True)

            create_user_profile.send(sender=BbUser.objects.get(
                username=register_form.cleaned_data.get('username')
            ))  # lesson_42_hw

            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = RegisterUserForm()

    context = {
        'title': title,
        'register_form': register_form,
    }

    return render(request, 'authapp/register.html', context)


def logout(request):
    user_logout.send(sender=request.user)  # lesson_42_hw

    auth.logout(request)

    return HttpResponseRedirect(reverse('index'))


class PasswordChangeRedirectView(RedirectView):
    url = reverse_lazy('password_change')


@api_view(['GET', 'POST'])
def api_users(request):
    if request.method == 'GET':
        users = BbUser.objects.all()
        serializer = BbUserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BbUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class APIBbUsers(APIView):  # lesson_52_hw
    def get(self, request):
        users = BbUser.objects.all()
        serializer = BbUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BbUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIBbUsersDel(APIView):  # lesson_52_hw
    def delete(self, request, username):
        user = BbUser.objects.get(username=username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class APIRubricViewSet(ModelViewSet):  # lesson_51_hw
    queryset = BbUser.objects.all()
    serializer_class = BbUserSerializer
