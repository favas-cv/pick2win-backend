

from rest_framework import serializers
from .models import Match
from tournaments.models import Tournaments, Team
from tournaments.serializers import TournamentsSerializer, TeamSerializer


class MatchSerializer(serializers.ModelSerializer):
    # Read
    tournament = TournamentsSerializer(read_only=True)
    home_team = TeamSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)

    # Write
    tournament_id = serializers.PrimaryKeyRelatedField(
        queryset=Tournaments.objects.all(),
        source="tournament",
        write_only=True
    )

    home_team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source="home_team",
        write_only=True
    )

    away_team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source="away_team",
        write_only=True
    )

    class Meta:
        model = Match
        fields = [
            "id",
            "tournament",
            "home_team",
            "away_team",
            "tournament_id",
            "home_team_id",
            "away_team_id",
            "home_score",
            "away_score",
            "kickoff",
            "is_finished",
            "prediction_lock_time",
        ]