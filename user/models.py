from django.db import models
from django.contrib.auth.models import AbstractUser

MANAGEMENT = "MANAGEMENT"
SALES = "SALES"
SUPPORT = "SUPPORT"

# Create your models here.
class User(AbstractUser):
    team_choices = [(MANAGEMENT, MANAGEMENT), (SALES, SALES), (SUPPORT, SUPPORT)]

    team = models.CharField(choices=team_choices, max_length=10)
