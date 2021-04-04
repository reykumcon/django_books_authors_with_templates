from django.shortcuts import render, redirect
from .models import Book, Author

def index_book(request):
    context = {
        'books_all': Book.objects.all()
    }
    return render(request, 'books.html', context)

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc']
        )
    return redirect('/books_authors/books')

def display_book(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book,
        'authors': Author.objects.exclude(books__id = id)
    }
    return render(request, 'book_details.html', context)

def assign_author(request, id):
    if request.method == 'POST':
        book = Book.objects.get(id=id)
        author = Author.objects.get(id=request.POST['author'])
        book.authors.add(author)
    return redirect(f'/books_authors/books/{id}')

def index_author(request):
    context = {
        'authors_all': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def add_author(request):
    if request.method == 'POST':
        Author.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes= request.POST['notes']
        )
    return redirect('/books_authors/authors')

def display_author(request, id):
    author = Author.objects.get(id=id)
    context = {
        'author': author,
        'books': Book.objects.exclude(authors__id = id),
    }
    return render(request, 'author_details.html', context)

def assign_author(request, id):
    if request.method == 'POST':
        author = Author.objects.get(id=id)
        book = Book.objects.get(id=request.POST['book'])
        author.books.add(book)
    return redirect(f'/books_authors/authors/{id}')