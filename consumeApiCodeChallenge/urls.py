from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from .views import CombatActionView

# router = routers.DefaultRouter()
# router.register('combat_action', CombatActionView.as_view(), basename="CombatAction")

urlpatterns = [
    url(r'^combat_action/$', CombatActionView.as_view()),
]