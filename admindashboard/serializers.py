from rest_framework import serializers
from clubs.models import Club
from accounts.models import User

class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields =["id","name", "place", "created_at", "is_active"]
        
class Userserializer(serializers.ModelSerializer):
    
    class Meta:
        model =User
        fields = ["name","phone","total_points","is_active"]
        
        
from matches.models import Match

class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Match
        fields ='__all__'

class UpdateScoreMatchScoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Match
        fields = ["away_score","home_score","is_finished"]
        
        