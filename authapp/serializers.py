from rest_framework import serializers
from .models import BbUser


class BbUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BbUser
        fields = ('username', 'email')
