# myapp/serializers.py
from rest_framework import serializers
from .models import Creature # Make sure to import your actual model

class CreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = '__all__' # Start by including all fields
        # Later, you can be more specific: fields = ['id', 'name', 'description', ...]