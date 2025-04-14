from rest_framework import serializers

class UserHomeSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})  
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=[("male", "Male"), ("female", "Female")])
    subscribe = serializers.BooleanField()


class UserSchoolFanSerializer(serializers.Serializer):
    name = serializers.CharField()
    location = serializers.CharField()
    
    