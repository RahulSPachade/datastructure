from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, get_object_or_404, redirect

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a page displaying all books
    else:
        form = BookForm()

    return render(request, 'create_book.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a page displaying all books
    else:
        form = BookForm(instance=book)

    return render(request, 'update_book.html', {'form': form, 'book': book})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')  # Redirect to a page displaying all books
