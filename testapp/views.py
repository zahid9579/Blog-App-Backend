from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

# To Register a new user
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
