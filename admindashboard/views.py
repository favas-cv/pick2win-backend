from accounts.models import User
from clubs.models import Club, Club_member


from rest_framework.generics import ListAPIView
from .serializers import ClubSerializer,Userserializer,UpdateScoreMatchScoreSerializer,MatchesSerializer
from matches.models import Match
from rest_framework.viewsets import ModelViewSet

from tournaments.models import Tournaments,Team
from tournaments.serializers import TeamSerializer,TournamentsSerializer
from matches.serializers import MatchSerializer
from leaderboard.models import Leaderboard
from leaderboard.serializers import LeaderboardSerializer


class TournamentsAdminView(ModelViewSet):
    queryset = Tournaments.objects.all()
    serializer_class = TournamentsSerializer


class TeamsAdminView(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer



class MatchAdminView(ModelViewSet):
    
        queryset = Match.objects.all().select_related("tournament", "home_team", "away_team")
        serializer_class = MatchSerializer


class GlobalLeaderboardView(ListAPIView):
    
    queryset = Leaderboard.objects.all().select_related("user").order_by("-total_points")
    serializer_class = LeaderboardSerializer



class AllClubsView(ModelViewSet):
    
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    
    
class AllUsersView(ListAPIView):
    
    queryset = User.objects.filter(role__in=["user","club_admins"])
    serializer_class = Userserializer
    
# class AllMatchesView(ListAPIView):
#     queryset=Match.objects.all()
#     serializer_class = MatchesSerializer  
    
from rest_framework.views import APIView 
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .tasks import calculate_match_points

class UpdateMatchScoreView(APIView):

    def patch(self, request, match_id):

        try:
            match = Match.objects.get(id=match_id)

        except Match.DoesNotExist:
            return Response(
                {"error": "Match not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UpdateScoreMatchScoreSerializer(
            match,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            # TODO: Trigger point calculation task here
            
            success,message = calculate_match_points(match_id=match.id)
            
            if not success:
                return Response({"error":message})

            return Response({
                "msg":message,
                "data":serializer.data})

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
        
        
