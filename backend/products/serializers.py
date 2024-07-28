from rest_framework import serializers
from .models import Product, Production

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'about', 'kind']

class ProductionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Production
        fields = ['id', 'headline', 'product']

