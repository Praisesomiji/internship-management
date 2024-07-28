from rest_framework import serializers
from .models import Team, Unit
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class TeamSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Team
        fields = ['id', 'group', 'description']

class UnitSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)

    class Meta:
        model = Unit
        fields = ['id', 'name', 'teams']

