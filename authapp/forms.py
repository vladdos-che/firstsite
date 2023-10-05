from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import Form, CharField
from django import forms
import re

from authapp.models import BbUser
from django.contrib.auth import get_user_model


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = BbUser
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    # password1 = forms.CharField(label='Пароль')
    # password2 = forms.CharField(label='Пароль (повторно)')

    # def clean_username(self):  # lesson_26_hw
    #     val = self.cleaned_data['username']
    #     if val[0] == '@':
    #         raise ValidationError('Первым символом нельзя использовать @!')
    #     if val[-1] != '@':
    #         raise ValidationError('Последним символом должен быть @!')
    #     return val

    # def clean(self):  # lesson_26_hw
    #     super().clean()
    #     errors = {}
    #     if not re.match(r'[A-Z]', self.cleaned_data['password1']):
    #         errors['password1'] = ValidationError('Нужна одна заглавная буква!')
    #     if errors:
    #         raise ValidationError(errors)

    class Meta:
        model = BbUser
        # fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'age')
        fields = ('username', 'email', 'first_name', 'last_name',)
