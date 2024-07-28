from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    kind = models.CharField(max_length=20, choices=[('crop', 'Crop'), ('livestock', 'Livestock')])

class Production(models.Model):
    headline = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

