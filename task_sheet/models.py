from django.db import models


class Task(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Задание",
    )

    content = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание",
    )

    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Опубликовано",
    )

    do_before_date = models.DateField(
        verbose_name="Сделать_до",
    )

    def __str__(self):
        return f'Задание: {self.title}'

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
        ordering = ['-published', 'title']
