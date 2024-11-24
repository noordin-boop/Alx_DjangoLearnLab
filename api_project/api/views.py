from rest_framework.generics import ListAPIView  # Ensure this is imported
from .models import Book
from .serializers import BookSerializer

# A view to list all books using DRF's generic ListAPIView
class BookList(ListAPIView):  # Ensure this inherits from ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
