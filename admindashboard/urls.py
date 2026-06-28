from .views import( AllClubsView,AllUsersView,
                   UpdateMatchScoreView,
                   TeamsAdminView,TournamentsAdminView,
                   MatchAdminView,GlobalLeaderboardView,
                   
                   )
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    r'tournaments',
    TournamentsAdminView,
    basename='tournaments'
)

router.register(
    r'teams',
    TeamsAdminView,
    basename='teams'
)
router.register(
    r'matches',
    MatchAdminView,
    basename='matches'
)
router.register(
    r'clubs',
    AllClubsView,
    basename='clubs'
)

urlpatterns = [
    # path('clubs/',AllClubsView.as_view()),
    path('users/',AllUsersView.as_view()),
    path('global-leaderboard/',GlobalLeaderboardView.as_view()),

    path('update-score/<int:match_id>/',UpdateMatchScoreView.as_view()),
] + router.urls 

