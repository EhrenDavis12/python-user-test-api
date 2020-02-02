from django.contrib.auth.models import User, Group
from quickstart.models import AppUser
from rest_framework import serializers


class AppUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'username', 'last_login',
                  'login_count', 'project_count']
