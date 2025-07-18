from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import ClothingItemViewSet


router = DefaultRouter()
router.register(r'items', ClothingItemViewSet, basename='clothingitem')

urlpatterns = [
    path('', include(router.urls)),
]
