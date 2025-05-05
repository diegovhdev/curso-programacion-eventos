from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JugadorViewSet

router = DefaultRouter()
router.register(r'jugadores', JugadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]