from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate, logout
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken

class Login(APIView):
    def post(self, request, format=None):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token),'user_id': user.id, 'username': user.username}, status=status.HTTP_200_OK)
        return Response({'message': '아이디 혹은 비밀번호가 잘못되었습니다'}, status=status.HTTP_400_BAD_REQUEST)

class Signup(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)

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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = OpinionSerializer

    def get(self, request, pk, format=None):
        opinions = Opinion.objects.filter(post_id = pk)
        data = []
        for n in range(0, len(opinions)):
            data.append({
                'id': opinions[n].id,
                'opinion_content': opinions[n].opinion_content,
                'post_content': opinions[n].post_content,
                'user': opinions[n].user.username
            })
        return Response(data)

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

class CommentList(APIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, pk, format=None):
        comments = Comment.objects.filter(opinion_id = pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        data = {
            'opinion' : pk,
            'comment_content': request.data['comment_content'],
            'from_user': request.data['from_user'],
            'to_user': request.data['to_user']
        }
        serializer = CommentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            if request.data['from_user'] != request.data['to_user']:
                from_user = User.objects.get(pk=request.data['from_user'])
                to_user = User.objects.get(pk=request.data['to_user'])
                body = from_user.username + '님이 ' + request.data['comment_content'] + ' 라고 답장하셨습니다.'
                email = EmailMessage(
                    'doyeong blog에 작성하신 댓글에 대한 답장입니다.', 
                    body, 
                    to=[to_user.email]
                )
                email.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)