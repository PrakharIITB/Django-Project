from dataclasses import fields
from rest_framework import serializers
from Home.models import team

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = "__all__"