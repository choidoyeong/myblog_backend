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
        category = Category.objects.get(category_name = name)
        posts = Post.objects.filter(category = category)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostList(APIView):
    
    def get(self, request, fromat=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetail(APIView):

    def get(self, request, pk, format = None):
        try:
            post = Post.objects.get(pk= pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)