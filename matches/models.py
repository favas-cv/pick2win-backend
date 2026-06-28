from django.db import models

# Create your models here.
from tournaments.models import Tournaments,Team


class Match(models.Model):
    
    tournament= models.ForeignKey(Tournaments,on_delete=models.CASCADE)
    home_team= models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team1')
    away_team= models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team2')
    kickoff = models.DateTimeField()
    home_score = models.IntegerField(null=True,blank=True)
    away_score = models.IntegerField(null=True,blank=True)
    
    prediction_lock_time = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    
    
 