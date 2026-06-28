from rest_framework import serializers
from clubs.models import Club_member,Club




class ClubSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Club
        fields ='__all__'
        
   

class ClubMemberSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source="user_id.name")

    class Meta:
        model = Club_member
        fields = [
            "id",
            "user_name",
            "role",
            "joined_at"
        ]