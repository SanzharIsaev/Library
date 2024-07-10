from django.urls import path, include


urlpatterns = [
    path('', include('apps.authors.urls')),
    path('', include('apps.books.urls')),
    path('', include('apps.users.urls')),
]
