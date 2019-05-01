from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category_name')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        feilds = ('id', 'post_title', 'post_content', 'category', 'like')

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ('id', 'post', 'opinion_content', 'post_content', 'user')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'from_user', 'to_user')