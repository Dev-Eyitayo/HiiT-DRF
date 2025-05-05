from django.shortcuts import render
from rest_framework import views, status, generics
from rest_framework.response import Response
from user.serializers import UserHomeSerializer, UserSchoolFanSerializer


class UserHomeView(generics.GenericAPIView):
    serializer_class = UserHomeSerializer
    
    def get(self, request):
        text = {"message": "Welcome Home"}
        return Response(status=status.HTTP_200_OK)
    
    def post (self,request) :
        return Response (data ={"message":"Data recived"}, status=201)
    
    def delete (self,request):
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    
    
class UserSchoolView(generics.GenericAPIView):
    serializer_class = UserSchoolFanSerializer
    
    def post(self, request):
        return Response(data = {"message": "Done"}, status=201)
    
class UserFanView(generics.GenericAPIView):
    serializer_class = UserSchoolFanSerializer
    
    def post(self, request):
        return Response(data = {"message": "Data received"}, status=201)

    def get(self, request):
        return Response(status=status.HTTP_200_OK) 