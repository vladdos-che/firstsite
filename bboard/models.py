from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from precise_bbcode.fields import BBCodeTextField


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


class RubricQuerySet(models.QuerySet):
    def order_by_bb_count(self):
        return self.annotate(cnt=models.Count('bb')).order_by('-cnt')


class RubricManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset().order_by('name')
        return RubricQuerySet(self.model, using=self._db)

    def order_by_bb_count(self):
        # return super().get_queryset().annotate(
        #     cnt=models.Count('bb')
        # ).order_by('-cnt')
        return self.get_queryset().order_by_bb_count()


class Rubric(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name="Название",)

    # objects = RubricManager()
    # objects = RubricQuerySet.as_manager()
    objects = models.Manager.from_queryset(RubricQuerySet)()

    # bbs = RubricManager()

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
            super().delete(*args, **kwargs)
        # Выполняем действия после удаления

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']


class BbManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('price')


class Bb(models.Model):
    KINDS = (
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Поменяю')
    )

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

    kind = models.CharField(
        max_length=1,
        choices=KINDS,
        default='s',
    )

    # content = models.TextField(
    content = BBCodeTextField(
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

    objects = models.Manager()
    by_price = BbManager()

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


def positive_num_validator(val):
    if val < 0:
        raise ValidationError(f'Число {val} меньше 0', code='negative')


class IceCreamKiosk(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name="Название киоска",
    )

    def __str__(self):
        return self.name

    def get_sum_id(self):
        return self.pk + self.pk

    class Meta:
        verbose_name = 'Киоск с мороженным'
        verbose_name_plural = 'Киоски с мороженным'
        ordering = ['name']


class IceCream(models.Model):
    kiosk = models.ForeignKey(
        'IceCreamKiosk',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Рубрика',
    )

    title = models.CharField(
        max_length=50,
        verbose_name="Название мороженого",
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
        validators=[positive_num_validator],
    )

    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Добавлено",
    )

    compound = models.TextField(
        null=True,
        blank=True,
        verbose_name="Состав",
        default="Секрет фирмы",
    )

    quantity = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Количество",
        default=0,
    )

    def __str__(self):
        return f'Мороженое: {self.title}'

    def get_sum_id_price(self):
        return self.pk + self.price

    class Meta:
        verbose_name = "Мороженое"
        verbose_name_plural = "Мороженые"
        ordering = ['-published', 'title']


class Parent(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Имя",
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание",
    )

    was_born = models.DateTimeField(
        db_index=True,
        null=True,
        blank=True,
        verbose_name="Родился",
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Возраст",
        default=0,
    )

    def __str__(self):
        return self.name

    def get_sum_id(self):
        return self.pk + self.pk

    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"
        ordering = ['-age', 'name']


class Child(models.Model):
    parent = models.ForeignKey(
        'Parent',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Родитель',
    )

    name = models.CharField(
        max_length=30,
        verbose_name="Имя",
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание",
    )

    was_born = models.DateTimeField(
        db_index=True,
        null=True,
        blank=True,
        verbose_name="Родился",
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Возраст",
        default=0,
    )

    def __str__(self):
        return self.name

    def get_sum_id(self):
        return self.parent.pk + self.pk

    class Meta:
        verbose_name = "Ребёнок"
        verbose_name_plural = "Дети"
        ordering = ['-age', 'name']
