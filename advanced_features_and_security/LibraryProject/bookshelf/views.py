# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required
from django.db import DatabaseError
from .models import Book
from .forms import ExampleForm


# View to list all books
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    try:
        books = Book.objects.all()
        return render(request, 'bookshelf/book_list.html', {'books': books})
    except DatabaseError:
        return HttpResponse("An error occurred while fetching the books.", status=500)


# View to create a book
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('book_list')
            except DatabaseError:
                return HttpResponse("An error occurred while saving the book.", status=500)
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})


# View to edit a book
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            try:
                form.save()
                return redirect('book_list')
            except DatabaseError:
                return HttpResponse("An error occurred while updating the book.", status=500)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})


# View to delete a book
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        try:
            book.delete()
            return redirect('book_list')
        except DatabaseError:
            return HttpResponse("An error occurred while deleting the book.", status=500)
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
