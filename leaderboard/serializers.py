from rest_framework import serializers
from .models import Leaderboard

class LeaderboardSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.name",
        read_only=True
    )

    class Meta:
        model = Leaderboard
        fields = [
            "user",
            "username",
            "total_points"
        ]
        