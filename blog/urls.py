from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, CategoryViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"article", ArticleViewSet)
router.register(r"category", CategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
