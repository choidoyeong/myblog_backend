from django.urls import include, path
from . import views

urlpatterns = [
    path('categorys/', views.CategoryList.as_view()),
    path('categorys/<str:name>/', views.CategoryDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/opinions/', views.OpinionList.as_view()),
]