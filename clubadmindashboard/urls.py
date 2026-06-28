

from django.urls import path
from .views import ClubMembersView,GenerateInviteLinkView

urlpatterns = [
     path('members/',ClubMembersView.as_view()),
     path('generate-link/',GenerateInviteLinkView.as_view()),
]
