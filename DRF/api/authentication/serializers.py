from rest_framework import serializers
from user.models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed



class SignUpSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    date_of_birth = serializers.DateField()
    gender = serializers.ChoiceField(choices = ['MALE', 'FEMALE'])
    profile_picture = serializers.ImageField(required = False)
    phone = serializers.CharField()
    nationality = serializers.CharField()
    address = serializers.CharField(required = False)
    user_type = serializers.ChoiceField(choices = ['CUSTOMER', 'RIDER', 'STAFF', 'ADMIN'])
    
    
    class Meta:
        model = CustomUser
        fields = ('firstname', 'lastname', 'email', 'password','phone', 'date_of_birth','address', 'user_type', 'nationality', 'gender', 'profile_picture')
        
        
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'tokens']
        
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        print(CustomUser.objects.filter(email=email).first().password)
        # user = auth.authenticate(email=email, password=password)
        user = CustomUser.objects.filter(email=email, password=password).first()
        if not user:
            raise AuthenticationFailed("Invalid login credentials")
        return {
            'id': user.id,
            'email': user.email,
            'tokens': user.tokens,
        }
        
        