from django.contrib import admin
from .models import Book,BookRequest

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")

@admin.register(BookRequest)
class BookRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "status", "created_at")
    list_filter = ("status",)