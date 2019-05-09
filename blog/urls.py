from django.urls import include, path
from . import views

urlpatterns = [
    path('categorys/', views.CategoryList.as_view()),
    path('categorys/<str:name>', views.CategoryDetail.as_view()),
]