from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
from business.serializers import BusinessSerializer
from rest_framework.permissions import IsAuthenticated

class BusinessView(generics.GenericAPIView):
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(owner = request.user)
        return Response(data = serializer.data, status=201)