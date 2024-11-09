from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.
from .models import Book
from .models import Library


def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Use library_detail.html for rendering
    context_object_name = 'library'  # Context variable for the library instance