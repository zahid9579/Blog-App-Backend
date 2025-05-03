from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, PostSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import Post

# To Register a new user
class RegisterView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.get_or_create(user=user)
            return Response({'msg': "User created successfully", "user": serializer.data},  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Login with email and password
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
       email = request.data.get("email")
       password = request.data.get("password")
       
       user = authenticate(request, email=email, password=password)
       
       if user is not None:
           token, created = Token.objects.get_or_create(user=user)
           return Response({"msg": "Login successfully", "token": token.key}, status=status.HTTP_200_OK)
       else:
           return Response({"error": "email or password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
       
       
       
# To Logout user
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"User Logged out successfully"}, status=status.HTTP_200_OK)
    

# CRUD for BLOG_API
# To create a post
class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
       serializer = PostSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save(author=request.user)
           return Response({"msg": "Post created successfully", "Post": serializer.data}, status=status.HTTP_201_CREATED)
       return Response({"msg": "Something went wrong", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# To get the list of Posts
class GetAllPostsView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data}, status=status.HTTP_200_OK)
    


# To update a POST
class UpdatePostView(APIView):
    permission_classes=[AllowAny]
    authentication_classes = [TokenAuthentication]

    def put(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            
        except post.DoesNotExist:
            return Response({'msg': "post not found"}, status=status.HTTP_404_NOT_FOUND)

        if post.author != request.user:
            return Response({"msg": "You are not allow to edit this post"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Post updated successfully", "updated post": serializer.data,},  status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# To delete a POST
class DeletePostView(APIView):
    permission_classes=[AllowAny]
    authentication_classes=[TokenAuthentication]
    
    def delete(self, request, pk):
        try: 
            post = Post.objects.get(pk=pk)
        except post.DoesNotExist:
            return Response({"msg": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        if post.author != request.user:
            return Response({"msg": "You are not allowed to delete this post"})
        
        post.delete()
        return Response({"msg": "Post has been deleted successfully"})
    


