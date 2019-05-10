from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CategoryList(APIView):
    serializer_class = CategorySerializer

    def get(self, request, format=None):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):

    def get(self, request, name, format=None):
        posts = Post.objects.filter(category = name)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

class PostList(APIView):
    
    def get(self, request, fromat=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)