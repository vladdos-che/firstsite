from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from bboard.models import Bb


@receiver(post_save, sender=Bb)
def post_save_dispatcher(created, **kwargs):
    instance = kwargs['instance']

    if created:
        print(f'Объявление {instance.title} создано!')
    else:
        print(f'Объявление {instance.title} изменено!')


# class SomeClass:
#     def post_save_dispatcher(self, sender, **kwargs):
#         # Тело метода-обработчика


add_bb = Signal()


def add_bb_dispatcher(sender, **kwargs):
    rubric = sender.rubric
    price = sender.price
    print(f'Объявление в рубрике "{rubric}" с ценой {price:.2f} создано')


add_bb.connect(add_bb_dispatcher)
