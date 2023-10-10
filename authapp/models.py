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


class Profile(models.Model):  # lesson_42_hw
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Создано",
    )

    user = models.ForeignKey(
        'BbUser',
        null=True,
        on_delete=models.DO_NOTHING,
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
