from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            user1 = User.objects.create_user('ivanov', password='1234567890', email='ivanov@site.kz')
            user2 = User.objects.create_user('petrov', password='0987654321', email='petrov@site.kz', is_staff=True)
            user3 = User.objects.create_superuser('sidorov', password='0987654321', email='sidorov@site.kz')
        except Exception as ex:
            print('Users are created')
            print(ex)
