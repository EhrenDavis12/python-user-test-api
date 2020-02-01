from django.contrib.auth.models import User, Group
from quickstart.models import AppUser
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, AppUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AppUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows view or edit of app users
    """
    queryset = AppUser.objects.all().order_by('last_login')
    serializer_class = AppUserSerializer
    http_method_names = ['get']


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
