from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.validators import FileExtensionValidator

# from authapp.models import BbUser
from bboard.models import Rubric, get_timestamp_path


# class AdvUser(User):  # использовать для расширения стандартного юзера  lesson_46
#     phone = models.CharField(max_length=20)
#
#     class Meta:
#         proxy = True


# class Spare(models.Model):
#     name = models.CharField(max_length=30)


# class Machine(models.Model):
#     name = models.CharField(max_length=30)
#     spares = models.ManyToManyField(Spare, through='Kit', through_fields=('machine', 'spare'))
#     notes = GenericRelation('Note')


# class Kit(models.Model):
#     machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
#     spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
#     count = models.IntegerField()


# class SMS(models.Model):
#     comment = models.CharField(max_length=120)
#
#     sender = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="sender"
#     )
#
#     receiver = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="receiver"
#     )


# class Hospital(models.Model):
#     name = models.CharField(max_length=50)
#     doctors = models.ManyToManyField('Doctor', through='Work', through_fields=('hospital', 'doctor'))
#
#
# class DoctorQuerySet(models.QuerySet):  # lesson_31_hw
#     def order_by_first_name(self):
#         return self.order_by('price')
#
#
# class Doctor(models.Model):
#     first_name = models.CharField(max_length=30)
#     past_name = models.CharField(max_length=30)
#     full_name = models.CharField(max_length=90,
#                                  default=f'{first_name} {past_name}')
#
#
# # doctors_by_name = Doctor.objects.all().order_by_first_name()  # lesson_31_hw
#
#
# class Work(models.Model):
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


# class Note(models.Model):
#     content = models.TextField()
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')
#
#     class Meta:
#         permissions = (
#             ('hide_comments', 'Можно скрывать комментарии'),
#         )


# class Message(models.Model):
#     content = models.TextField()


# class PrivateMessage(Message):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.OneToOneField(Message, on_delete=models.CASCADE, parent_link=True)


# class Message(models.Model):
#     content = models.TextField()
#     name = models.CharField(max_length=20)
#     email = models.EmailField()
#
#     class Meta:
#         abstract = True
#         ordering = ['name']


# class PrivateMessage(Message):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#     email = None
#
#     class Meta(Message.Meta):
#         pass


# class RevRubric(Rubric):
#     class Meta:
#         proxy = True
#         ordering = ['-name']


class Img(models.Model):
    img = models.ImageField(
        verbose_name='Изображение',
        upload_to=get_timestamp_path,
        validators=[FileExtensionValidator(allowed_extensions=('jpg', 'png', 'gif'))]
    )

    desc = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
