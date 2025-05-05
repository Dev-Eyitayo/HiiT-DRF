from rest_framework import serializers
from .models import Business

class BusinessSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    street = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=25)
    logo = serializers.ImageField()
    class Meta:
        model = Business
        fields = ['id', 'name', 'logo', 'type', 'country', 'state', 'street', 'phone', 'created_at', 'city' ]