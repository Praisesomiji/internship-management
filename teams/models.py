from django.db import models
from django.contrib.auth.models import Group

class Team(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.group.name

class Unit(models.Model):
    name = models.CharField(max_length=255)
    teams = models.ManyToManyField(Team)
