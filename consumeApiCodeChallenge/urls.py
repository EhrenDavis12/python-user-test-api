from django.urls import path, re_path
from rest_framework import routers
from .views import CombatActionView

# router = routers.DefaultRouter()
# router.register('combat_action', CombatActionView.as_view(), basename="CombatAction")

urlpatterns = [
    re_path(r'^combat_action/$', CombatActionView.as_view()),
]