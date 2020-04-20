from rest_framework import serializers
from .models import Trail

class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ('title','about','date','author','region','distance','difficulty','image','track')