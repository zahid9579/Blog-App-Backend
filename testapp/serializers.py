from rest_framework import serializers
from .models import User, Post


# User Seralizer
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model=User
        fields = ['id', 'name', 'email', 'password', 'date_of_birth']
        extra_kwargs = {'password': {'write_only': True}}
        
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],  
            date_of_birth=validated_data['date_of_birth']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    



# Post Serializer 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id', 'title', 'content', 'author']