from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def get_min_length():
    min_length = 3
    return min_length


def validate_even(val):
    if val % 2 != 0:
        raise ValidationError('Число %(value)s нечётное', code='odd', params={'value': val})


# class MinMaxValueValidator:
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def __call__(self, val):
#         if val < self.min_value or val > self.max_value:
#             raise ValidationError('Введёное чило должно быть > %(min)s и < %(max)s', code='out_of_range',
#                                   params={'min': self.min_value, 'max': self.max_value})


class Rubric(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name="Название",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return "/bboard/%s/" % self.pk
        # return f"/bboard/{self.pk}/"
        return f"/{self.pk}/"

    def save(self, *args, **kwargs):
        # Выполняем действия до сохраения
        if True:
            super().save(*args, **kwargs)
        # Выполняем действия после сохраения

    def delete(self, *args, **kwargs):
        # Выполняем действия до удаления
        if True:
            super().save(*args, **kwargs)
        # Выполняем действия после удаления

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']


class Bb(models.Model):
    rubric = models.ForeignKey(
        'Rubric',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Рубрика',
    )

    title = models.CharField(
        max_length=50,
        verbose_name="Товар",
        validators=[validators.MinLengthValidator(get_min_length)],
        # validators=[validators.ProhibitNullCharactersValidator()],  # \x00
        error_messages={'min_length': 'Слишком мало символов, min: 3'},
    )

    content = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание",
    )

    price = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Цена",
        # validators=[validate_even, MinMaxValueValidator(50, 60_000_000)],
    )

    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Опубликовано",
    )

    def __str__(self):
        return f'Объявление: {self.title}'

    def title_and_price(self):
        if self.price:
            return f"{self.title} ({self.price:.2f})"
        return self.title

    class Meta:
        # order_with_respect_to = 'rubric'
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-published', 'title']
