from django.db import models

# Create your models here.
class team(models.Model):
    teamId = models.CharField(max_length=50)
    teamName = models.CharField(max_length=50)
    player1 = models.CharField(max_length=50)
    player2 = models.CharField(max_length=50)
    player3 = models.CharField(max_length=50)
    player4 = models.CharField(max_length=50)
    def __str__(self):
        return self.teamName