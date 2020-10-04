from django.views.generic import DetailView, ListView

from .models import Book


class BookListView(ListView):
    model = Book
    # context_object_name = 'book_list' # Not required
    # template_name = 'books/book_list.html' # Not required


class BookDetailView(DetailView):
    model = Book
    # context_object_name = 'book'
    # template_name = 'books/book_detail.html'