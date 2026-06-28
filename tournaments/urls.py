from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    TournamentsView,
    TeamsView
)

router = DefaultRouter()

router.register(
    r'tournaments',
    TournamentsView,
    basename='tournaments'
)

router.register(
    r'teams',
    TeamsView,
    basename='teams'
)

urlpatterns = [
    path('', include(router.urls)),
]