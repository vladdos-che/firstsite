from django.dispatch import Signal, receiver

from authapp.models import Profile


create_user_profile = Signal()


def user_profile_dispatcher(sender, **kwargs):  # lesson_42_hw
    try:
        Profile.objects.create(user=sender)
    except:
        print('уже создано')
    else:
        print('создано')


create_user_profile.connect(user_profile_dispatcher)


def user_logout_dispatcher(sender, **kwargs):  # lesson_42_hw
    print(f'Пользователь {sender.username} вышел')


user_logout = Signal()
user_logout.connect(user_logout_dispatcher)
