from rest_framework.generics import ListAPIView  # Ensure this is imported
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# A view to list all books using DRF's generic ListAPIView
class BookList(generics.ListAPIView):  # Ensure this inherits from ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
