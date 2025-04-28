from django.shortcuts import render
from rest_framework import views, status, generics
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import views, status, generics
from rest_framework.response import Response
from authentication.serializers import SignUpSerializer, LoginSerializer
from user.models import CustomUser
# from django.contrib.auth import authenticate

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        phone = serializer.validated_data.get("phone")
        password = serializer.validated_data.get("password")
        user_exist = CustomUser.objects.filter(email=email).first()
        if user_exist:
            return Response({"error": "Email already exists"}, status=400)
        phone_exist = CustomUser.objects.filter(phone=phone).first()
        if phone_exist:
            return Response({"error": "Phone Number already exists"}, status=400)
        
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=201)
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data = serializer.data, status=200)