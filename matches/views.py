from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Match
from .serializers import MatchSerializer


class AllMatchView(ReadOnlyModelViewSet):
    
        queryset = Match.objects.all().select_related("tournament", "home_team", "away_team")
        serializer_class = MatchSerializer


        