from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Book

class BookListView(ListView):
    model = Book
    template_name = '_books.html'
    context_object_name = 'books'

def delete(request, book_id):
    books = get_object_or_404(Book, pk=book_id)
    print(books)
    books.delete()
    return render(request, 'books.html')

        