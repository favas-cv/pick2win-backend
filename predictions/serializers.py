from rest_framework import serializers
from .models import Prediction
from matches.models import Match
from matches.serializers import MatchSerializer


class PredictionSerializer(serializers.ModelSerializer):

    match_id = serializers.PrimaryKeyRelatedField(
        queryset=Match.objects.all(),
        source="match",
        write_only=True
    )

    match = MatchSerializer(read_only=True)

    class Meta:
        model = Prediction
        fields = (
            "id",
            "match",
            "match_id",
            "home_prediction",
            "away_prediction",
            "points",
            "is_calculated",
            "created_at"
        )

        read_only_fields = (
            "points",
            "is_calculated",
            "created_at"
        )