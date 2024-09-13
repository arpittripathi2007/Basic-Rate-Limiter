from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    rate_limit = models.IntegerField(default=100)

class RateLimitUser(models.Model):
    username = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    ) 
    name = models.CharField(max_length=200)
    rate_limit = models.IntegerField(default=100, null=False)