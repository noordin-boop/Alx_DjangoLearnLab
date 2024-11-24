from rest_framework.generics import ListAPIView  # Ensure this is imported
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# A view to list all books using DRF's generic ListAPIView
class BookList(generics.ListAPIView):  # Ensure this inherits from ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 


    
