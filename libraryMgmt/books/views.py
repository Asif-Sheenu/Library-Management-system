from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, BookRequest
from .forms import BookForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {'form': form})


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_year = request.POST.get("published_year")
        book.save()

        return redirect("books:book_list")

    return render(request, "books/edit_book.html", {"book": book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect("books:book_list")


def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(
        Q(title__icontains=query) |
        Q(author__icontains=query)
    )
    return render(request, 'books/search_books.html', {'books': books, 'query': query})


@login_required
def request_book(request, id):
    book = get_object_or_404(Book, id=id)

    existing = BookRequest.objects.filter(
        user=request.user,
        book=book,
        status="PENDING"
    ).first()

    if existing:
        return redirect("books:my_requests")

    BookRequest.objects.create(
        user=request.user,
        book=book,
        status="PENDING"
    )

    return redirect("books:my_requests")


@login_required
def my_requests(request):
    requests = BookRequest.objects.filter(user=request.user)
    return render(request, 'books/my_requests.html', {'requests': requests})


def browse_books(request):
    books = Book.objects.all()
    return render(request, "books/browse.html", {"books": books})


def admin_requests(request):
    requests_list = BookRequest.objects.select_related('user', 'book').all()
    return render(request, 'admin/requests.html', {'requests': requests_list})


def update_request_status(request, id, action):
    book_request = get_object_or_404(BookRequest, id=id)

    if action == "approve":
        book_request.status = "APPROVED"
    elif action == "reject":
        book_request.status = "REJECTED"
    else:
        messages.error(request, "Invalid action.")
        return redirect('books:admin_requests')

    book_request.save()
    messages.success(request, f"Request has been {book_request.status.lower()}.")
    return redirect('books:admin_requests')
 
 
def user_profile(request):
    user = request.user

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.save()

    user_books = BookRequest.objects.filter(user=user)

    return render(request, "books/user_profile.html", {
        'user': user,
        'books': user_books
    })
