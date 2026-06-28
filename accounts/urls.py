from .views import LoginView,RegisterView,ProfileView,LogoutView,ClubRegisterView
from django.urls import path


urlpatterns = [
    path('login/',LoginView.as_view()),
    path('register/',RegisterView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('club-register/',ClubRegisterView.as_view()),
     path("profile/", ProfileView.as_view(), name="profile"),
]
