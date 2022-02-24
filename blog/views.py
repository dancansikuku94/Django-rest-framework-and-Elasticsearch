from django.shortcuts import render
from .models import Article, Category
from .serializer import UserSerializer, ArticleSerializer, CategorySerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
