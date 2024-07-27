from django.db import models
from teams.models import Team
from members.models import Profile

class Product(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    kind = models.CharField(max_length=20, choices=[('crop', 'Crop'), ('Livestock', 'Livestock')])

class Production(models.Model):
    headline = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
