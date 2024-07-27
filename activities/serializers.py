from rest_framework import serializers
from .models import Activity, Category, Trace
from products.serializers import ProductionSerializer
from teams.serializers import UnitSerializer, TeamSerializer
from members.serializers import ProfileSerializer

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'production', 'date', 'cost_in_naira', 'loss_or_mortality']

class CategorySerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'activities']

class TraceSerializer(serializers.ModelSerializer):
    productions = ProductionSerializer(many=True)
    unit = UnitSerializer()
    team = TeamSerializer()
    producer = ProfileSerializer()

    class Meta:
        model = Trace
        fields = ['id', 'productions', 'week', 'unit', 'team', 'producer']

