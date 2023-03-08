from rest_framework import serializers
from home.models import idea

class idea_serializer(serializers.ModelSerializer):
    class Meta:
        model = idea
        fields = '__all__'