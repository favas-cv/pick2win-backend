from .views import AllMatchView
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register(
    r'matches',
    AllMatchView,
    basename='teams'
)

urlpatterns = [
    path('', include(router.urls)),
]

