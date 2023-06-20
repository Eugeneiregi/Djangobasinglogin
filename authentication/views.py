from django.shortcuts import render
from httplib2 import Authentication
import authentication

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import authenticate

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Perform authentication
    user = authenticate (username=username, password=password)
    
    if user is not None:
        # Authentication successful
        response_data = {'message': 'Login successful'}
        return Response(response_data)
    else:
        # Authentication failed
        response_data = {'message': 'Invalid credentials'}
        return Response(response_data, status=401)
