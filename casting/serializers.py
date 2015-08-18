from .models import Actor, Casting
from rest_framework import serializers


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor


class CastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casting
