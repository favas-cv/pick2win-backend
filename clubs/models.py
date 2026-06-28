from django.db import models
from accounts.models import User
# Create your models here.


class Club(models.Model):
    
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='owned_clubs')
    
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    place = models.CharField(max_length=50)
    description = models.TextField()
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Club_member(models.Model):
    
    ROLE_CHOICES = (
        ('club_admin', 'Club Admin'),
        ('member', 'Member'),
    )
    
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=25,choices=ROLE_CHOICES)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    
import uuid    
    
class ClubInvite(models.Model):

    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )