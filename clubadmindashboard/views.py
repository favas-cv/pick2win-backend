from rest_framework.generics import ListAPIView

from accounts.models import User
from .serializers  import ClubMemberSerializer
from clubs.models import Club,Club_member

class ClubMembersView(ListAPIView):
    serializer_class = ClubMemberSerializer
    
    def get_queryset(self):
        
        my_club = Club_member.objects.filter(
            user_id = self.request.user.id,
            role ="club_admin"
        ).first()
        
        if not my_club:
            return Club_member.objects.none()
            
        return Club_member.objects.filter(
            club_id = my_club.club_id
        ).select_related("user")
        
        
        
from django.shortcuts import render

from clubs.models  import Club,Club_member,ClubInvite
from .serializers import ClubSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response



# clubowner  




  
class GenerateInviteLinkView(APIView):
    
    def post(self,request):
        
        club_id = request.data.get('club_id')
        if not club_id:
            return Response ({"error":"the clubid missing from you"})
        
        club = Club.objects.filter(id=club_id).first()
        
        if not club:
            return Response({"error":"the club not found"})
        
        invite = ClubInvite.objects.create(
            club=club
            # created_by = request.user
            # created_by = 'developer'
        )
        
        return Response({
    "invite_link": f"https://pick2win-f.vercel.app/register?token={invite.token}",
    "token": invite.token
})
    



        
    
    