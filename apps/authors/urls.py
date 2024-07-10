from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthorsAPIViews

router = DefaultRouter()
router.register(r'authors', AuthorsAPIViews)


urlpatterns = [
    path('', include(router.urls)),
]