from django.db import models

# Create your models here.


class Tournaments(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date= models.DateField()
    end_date=models.DateField()
    status = models.CharField(max_length=25)
    
    
    
class Team(models.Model):
    name = models.CharField(max_length=50)
    logo = models.URLField(blank=True,null=True)
    country_code = models.CharField(max_length=50)
    