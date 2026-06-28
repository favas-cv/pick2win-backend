from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Leaderboard
from .serializers import LeaderboardSerializer
from rest_framework.generics import ListAPIView

class ClubTournamentLeaderboardView(APIView):

    def get(self, request, club_id, tournament_id):

        leaderboard = (
            Leaderboard.objects.filter(
                club_id=club_id,
                tournament_id=tournament_id
            )
            .select_related("user")
            .order_by("-total_points")
        )

        serializer = LeaderboardSerializer(
            leaderboard,
            many=True
        )

        return Response(serializer.data)
    
    

    
    
