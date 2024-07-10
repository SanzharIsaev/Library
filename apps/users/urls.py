from django.urls import path, include, re_path

from .views import RegisterView, LoginView, LogoutView


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]