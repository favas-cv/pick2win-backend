from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    ROLE_CHOICES = (
        ("user", "User"),
        ("club_admin", "Club Admin"),
        ("admin", "Admin"),
    )
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="user"
    )
    
    name = models.CharField(max_length=60)
    phone= models.CharField(
        max_length=15,
        unique=True
    )
    total_points = models.IntegerField(default=0)
    

    