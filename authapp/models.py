from django.contrib.auth.models import AbstractUser
from django.db import models


class BbUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
        null=True,
        verbose_name='аватарка'
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='возраст'
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']
