from django.shortcuts import render
from authapp.models import User
from authapp.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# class RegisterView(APIView):
#     def post(self,request):
#         data=request.data
#         userserializer=UserSerializer(data=request.data)
#         if userserializer.is_valid():
#             userserializer.save()
#             return Response(userserializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(userserializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def registeruser(request):
    data = request.data
    userserializer=UserSerializer()






