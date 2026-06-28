from rest_framework.generics import ListAPIView
from .models import Prediction
from .serializers import PredictionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.utils import timezone

from clubs.models import Club_member
from django.shortcuts import get_object_or_404


class MyPredictionsView(ListAPIView):

    serializer_class = PredictionSerializer

    def get_queryset(self):

        return Prediction.objects.filter(
            user=self.request.user
        ).select_related(
            "match__tournament",
            "match__home_team",
            "match__away_team",
            "club"
        )
        
        



class CreatePredictionView(APIView):

    def post(self, request):

        serializer = PredictionSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        match = serializer.validated_data["match"]

        if timezone.now() > match.prediction_lock_time:
            raise ValidationError(
                "Prediction closed"
            )

        club_member = Club_member.objects.filter(
            user_id=request.user
        ).first()

        if not club_member:
            raise ValidationError(
                "Join a club first"
            )

        if Prediction.objects.filter(
            user=request.user,
            match=match,
            club=club_member.club
        ).exists():

            raise ValidationError(
                "Already predicted"
            )

        prediction = serializer.save(
            user=request.user,
            club=club_member.club
        )

        return Response(
            PredictionSerializer(prediction).data,
            status=status.HTTP_201_CREATED
        )
        
        


class UpdatePredictionView(APIView):

    def patch(self, request, pk):

        prediction = get_object_or_404(
            Prediction,
            id=pk,
            user=request.user
        )

        if timezone.now() > prediction.match.prediction_lock_time:
            raise ValidationError(
                "Prediction locked"
            )

        serializer = PredictionSerializer(
            prediction,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(serializer.data)
    
    
    
    