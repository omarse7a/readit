from django.db import models
from authentication.models import Profile

# Create your models here.

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Adventure', 'Adventure'), 
        ('Science fiction', 'Science fiction'),
        ('Thriller', 'Thriller'),
        ('Mystery', 'Mystery'),
        ('Horror', 'Horror'),
        ('Autobiographical', 'Autobiographical'),
        ('Fantasy', 'Fantasy'),
        ('Drama', 'Drama'),
        ('History', 'History'),
        ('Science', 'Science'),
    ]
    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Arabic', 'Arabic'),
        ('Spanish', 'Spanish'),
        ('French', 'French'),
    ]
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to="book-covers/%y/%m/%d")
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="Any", choices=CATEGORY_CHOICES,)
    no_of_pages = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=20, default="English", choices=LANGUAGE_CHOICES,)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    isAvailable = models.BooleanField(default=True)
    current_borrower = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='borrowed_books')

    def __str__(self):
        return self.title

class Borrowed(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile.user.username} borrowed {self.book.title}" #self.user.user.username
    class Meta:
        verbose_name = 'borrowed book'