from django.db import models
from teams.models import Unit, Team
from products.models import Production
from members.models import Profile

class Trace(models.Model):
    productions = models.ManyToMany(Production)
    week = models.IntegerField()
    unit = models.ForeignKey(Unit, null=True, blank=True, on_delete=models.SET_NULL)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    producer = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

class Category(models.Model):
    name = models.CharField(max_length=255)
    activities = models.ManyToMany(Activity)

class Activity(models.Model):
    name = models.CharField(max_length=255)
    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    cost_in_naira = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    loss_or_mortality = models.DecimalField(max_digits=10, default=0, decimal_places=2)

