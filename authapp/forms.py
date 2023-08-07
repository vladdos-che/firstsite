from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import Form, CharField


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserViewForm(Form):
    user_name = CharField(max_length=100)
