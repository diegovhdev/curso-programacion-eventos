from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideojuegosViewSet

router = DefaultRouter()
router.register(r'videojuegos', VideojuegosViewSet)

urlpatterns = [
    path('', include(router.urls))
]