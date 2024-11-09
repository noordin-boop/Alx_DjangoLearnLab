# relationship_app/views.py

from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Updated template path

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Updated template path
    context_object_name = 'library'
