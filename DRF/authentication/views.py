from django.shortcuts import render
from rest_framework import views, status, generics
from rest_framework.response import Response

class SignUpView(generics.GenericAPIView):
    