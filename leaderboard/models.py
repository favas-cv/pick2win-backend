from django.db import models

# Create your models here.
from accounts.models import User
from tournaments.models import Tournaments
from matches.models import Match
from clubs.models import Club

class Leaderboard(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournaments,on_delete=models.CASCADE)
    
    total_points  = models.IntegerField(default=0)
    
    class Meta:
        unique_together =(
            "user","club","tournament"
        ) 