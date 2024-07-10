from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookAPIViews

router = DefaultRouter()
router.register(r'books', BookAPIViews)


urlpatterns = [
    path('', include(router.urls)),
]