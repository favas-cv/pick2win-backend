from django.urls import path
from .views import ClubTournamentLeaderboardView


urlpatterns = [
    
path(
    "<int:club_id>/<int:tournament_id>/",
    ClubTournamentLeaderboardView.as_view()
),
# path("global/",GlobalLeaderboardView.as_view()), 

]
