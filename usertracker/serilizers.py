from rest_framework import serializers
from usertracker.models import UserTracer

class UserTracerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTracer
        fields = '__all__'
