from django.urls import path
from .views import (
    book_list, add_book, edit_book, delete_book,
    search_books, request_book, my_requests, browse_books,
    admin_requests, update_request_status,user_profile
)

app_name = 'books'

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('add/', add_book, name='add_book'),
    path('<int:id>/edit/', edit_book, name='edit_book'),
    path('<int:id>/delete/', delete_book, name='delete_book'),
    path('search/', search_books, name='search_books'),
    path('request/<int:id>/', request_book, name='request_book'),
    path('my-requests/', my_requests, name='my_requests'),
    path('browse/', browse_books, name='browse'),
    path('book-requests/', admin_requests, name='admin_requests'),
    path('profile/', user_profile, name='user_profile'),
    path('book-requests/<int:id>/<str:action>/', update_request_status, name='update_request_status'),
]
