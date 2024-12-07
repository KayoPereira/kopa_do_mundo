# type: ignore
from rest_framework import serializers
from .models import Team
from datetime import datetime


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "titles", "top_scorer", "fifa_code", "first_cup"]