from django.db import models

from tournaments.models import Tournaments,Team
from matches.models import Match
from accounts.models import User
from clubs.models import Club


class Prediction(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    home_prediction = models.IntegerField()
    away_prediction = models.IntegerField()
    points = models.IntegerField(default=0)
    is_calculated = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
      
    
    class Meta:
        unique_together = (
            "user",
            "match",
            "club"
        )
         