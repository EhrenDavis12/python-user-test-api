from django.contrib.auth.models import User, Group
from quickstart.models import AppUser
from rest_framework import viewsets
from quickstart.serializers import AppUserSerializer


class AppUserAllViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows view or edit of app users
    """
    queryset = AppUser.objects.all().order_by('last_login')
    serializer_class = AppUserSerializer
    http_method_names = ['get', 'patch']


class AppUserNonActiveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows view or edit of app users that are not active
    """
    queryset = AppUser.objects.filter(login_count=0)
    serializer_class = AppUserSerializer
    http_method_names = ['get']


class AppUserActiveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows view or edit of app users that are active
    """
    queryset = AppUser.objects.filter(login_count__gt=0)
    serializer_class = AppUserSerializer
    http_method_names = ['get']
