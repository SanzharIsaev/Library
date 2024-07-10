from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer
from config.permissions import IsAdminOrReadOnly


class BookAPIViews(viewsets.ModelViewSet):
    
    queryset = Book.objects.using('nonrel').all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)
