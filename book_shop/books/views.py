# from multiprocessing import context
from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import HttpRequest, HttpResponse

from .models import Book

# Create your views here.
books = [
    {'id': 1, 'title': 'Harry Potter and the Chamber of Secrets', 'author': 'J.K. Rowling',
        'number_of_pages': 352, 'price': 100, 'image': 'book1.png'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee',
        'number_of_pages': 326, 'price': 120, 'image': 'book2.png'},
    {'id': 3, 'title': '1984', 'author': 'George Orwell',
        'number_of_pages': 228, 'price': 200, 'image': 'book3.png'},
    {'id': 4, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald',
        'number_of_pages': 180, 'price': 50, 'image': 'book4.png'},
    {'id': 5, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger',
        'number_of_pages': 208, 'price': 100, 'image': 'book5.png'},
]


def books_list(request):
    books = Book.objects.all()
    context = {'title': 'All books', 'books': books}
    # return HttpResponse(json.dumps(books), content_type='application/json')
    return render(request, 'books/allbooks.html', context)


def book_detail(request, book_id):
    book = None
    book = Book.objects.get(id=book_id)
    if not book:
        return HttpResponse(json.dumps({'error': 'Book not found'}), content_type='application/json')
        # return render(request, 'books/bookDetails.html', context)
    context = {'book': book}
    return render(request, 'books/bookDetails.html', context)


def book_create(request: HttpRequest):
    if request.method == 'POST':
        try:
            # Get the form data
            title = request.POST.get('title')
            author = request.POST.get('author')
            number_of_pages = request.POST.get('number_of_pages')
            price = request.POST.get('price')
            image = request.FILES.get('image') or None
            book = Book(title=title, author=author,
                        number_of_pages=number_of_pages, price=price, image=image)
            book.save()
            return render(request, 'books/addBook.html', {'success': f'Book {title} added successfully'})
        except:
            return render(request, 'books/addBook.html', {'error': 'Please fill all the required fields', 'title': 'Add a new book'})
    else:
        context = {'title': 'Add a new book'}
        return render(request, 'books/addBook.html', context)


def book_edit(request, book_id):
    if request.method == 'POST':
        try:
            # Get the form data
            title = request.POST.get('title')
            author = request.POST.get('author')
            number_of_pages = request.POST.get('number_of_pages')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            book = Book.objects.get(id=book_id)
            book.title = title or book.title
            book.author = author or book.author
            book.number_of_pages = number_of_pages or book.number_of_pages
            book.price = price or book.price
            book.image = image
            book.save()
            return render(request, 'books/addBook.html', {'book': book, 'success': f'Book {title} updated successfully'})
        except:
            return render(request, 'books/addBook.html', {'error': 'Book not found'})
        # return render(request, 'books/addBook.html', {'error': 'Please fill all the required fields', 'title': 'Add a new book'})
    else:
        book = Book.objects.get(id=book_id)
        context = {'book': book, 'title': 'Edit book'}
        return render(request, 'books/addBook.html', context)


def book_delete(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        # delete the book image file
        if book.image:
            book.image.delete()
        book.delete()
        return render(request, 'books/allBooks.html', {'books': Book.objects.all(), 'success': f'Book {book.title} deleted successfully'})
    except:
        return render(request, 'books/allBooks.html', {'error': 'Book not found'})
