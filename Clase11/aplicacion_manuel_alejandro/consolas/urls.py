from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsolasViewSet

router = DefaultRouter()
router.register( r'consolas', ConsolasViewSet)

urlpatterns = [
    path( '', include(router.urls))
]
