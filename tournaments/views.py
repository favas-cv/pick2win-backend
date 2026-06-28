from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from tournaments.models import Tournaments, Team
from .serializers import (
    TournamentsSerializer,
    TeamSerializer
)


class TeamsView(ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
class TournamentsView(ReadOnlyModelViewSet):
    queryset = Tournaments.objects.all()
    serializer_class = TournamentsSerializer