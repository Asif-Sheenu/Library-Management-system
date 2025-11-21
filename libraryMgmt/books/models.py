from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
    title= models.CharField(max_length=200)
    author= models.CharField(max_length=200)
    description= models.TextField()
    published_year = models.IntegerField(default=0)
    def __str__(self):
        return self.title

User =get_user_model()

class BookRequest(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.book.title} ({self.status})"

    
    
