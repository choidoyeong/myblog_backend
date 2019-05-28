from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Login(APIView):
    def post(self, request, format):
        pass

class Signup(APIView):
    serializer_class = UserSerializer

    def post(self, request, format):
        pass

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

class OpinionList(APIView):
    serializer_class = OpinionSerializer

    def get(self, request, pk, format=None):
        opinions = Opinion.objects.filter(post_id = pk)
        serializer = OpinionSerializer(opinions, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        data = {
            'post': pk,
            'opinion_content': request.data['opinion_content'],
            'post_content': request.data['post_content'],
            'user': request.data['user']
        }
        serializer = OpinionSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)