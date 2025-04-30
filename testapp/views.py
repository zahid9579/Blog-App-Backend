from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny  
from django.contrib.auth import authenticate, logout

# To Register a new user
class RegisterView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "User created successfully"},  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Login with email and password
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
       email = request.data.get("email")
       password = request.data.get("password")
       
       user = authenticate(request, email=email, password=password)
       
       if user is not None:
           return Response({"msg": "Login successfully"}, status=status.HTTP_200_OK)
       
       else:
           return Response({"error": "email or password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
       
       
       
# To Logout user
class LogoutView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        logout(request)
        return Response({"User Logout"}, status=status.HTTP_200_OK)