from django.db import models


class MyUserManager(models.Manager):  # lesson_31_hw
    def get_queryset(self):
        return super().get_queryset().order_by('-name')


class MyUser(models.Model):  # lesson_19_hw
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name="Имя",)

    password = models.CharField(
        max_length=20,
        verbose_name="Пароль", )

    my_users = MyUserManager()  # lesson_31_hw

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мой Пользователь'
        verbose_name_plural = 'Мои Пользователи'
        ordering = ['name']
