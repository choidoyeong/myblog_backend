from django.urls import include, path
from . import views

urlpatterns = [
    path('categorys/', views.CategoryList.as_view()),
    path('categorys/<str:name>/', views.CategoryDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/opinions/', views.OpinionList.as_view()),
    path('opinions/<int:pk>/comments/', views.CommentList.as_view()),
    path('signup/', views.Signup.as_view()),
    path('login/', views.Login.as_view()),
]