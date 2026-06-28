from rest_framework import serializers
from .models import Tournaments,Team


class TournamentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tournaments
        fields = '__all__'
        
        
        
        
class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Team
        fields='__all__'
