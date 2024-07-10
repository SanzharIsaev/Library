from rest_framework import viewsets

from .models import Author
from .serializers import AuthorSerializer
from config.permissions import IsAdminOrReadOnly


class AuthorsAPIViews(viewsets.ModelViewSet):
    
    queryset = Author.objects.using('nonrel').all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminOrReadOnly,)
