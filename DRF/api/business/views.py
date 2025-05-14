from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
from business.serializers import BusinessSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Business
from utils.pagination import CustomPagination
from utils.permissions import IsFemaleUser
class BusinessView(generics.GenericAPIView):
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated, IsFemaleUser]
    pagination_class = CustomPagination
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(owner = request.user)
        return Response(data = serializer.data, status=201)
    
    def get_queryset(self):
        user = self.request.user
        user_business = Business.objects.filter(owner=user)
        return user_business
    
    def get(self, request):
        user = request.user
        businesses = self.get_queryset()
        page = self.paginate_queryset(businesses)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(businesses, many=True)
        return Response(data = serializer.data, status=200)
    