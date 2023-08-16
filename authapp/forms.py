from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Form, CharField
from django import forms
import re


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    # password1 = forms.CharField(label='Пароль')
    # password2 = forms.CharField(label='Пароль (повторно)')

    def clean_username(self):
        val = self.cleaned_data['username']
        if val[0] == '@':
            raise ValidationError('Первым символом нельзя использовать @!')
        if val[-1] != '@':
            raise ValidationError('Последним символом должен быть @!')
        return val

    def clean(self):
        super().clean()
        errors = {}
        if not re.match(r'[A-Z]', self.cleaned_data['password1']):
            errors['password1'] = ValidationError('Нужна одна заглавная буква!')
        if errors:
            raise ValidationError(errors)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        # fields = ('username', 'email', 'first_name', 'last_name')


class UserViewForm(Form):
    user_name = CharField(max_length=100)
