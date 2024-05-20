from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to="book-covers/%y/%m/%d")
    #cover = models.ImageField(upload_to="book-covers/%y/%m/%d", default="book-covers/24/05/14/frankenstein.jpeg")
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True, blank=True, default='Uncategorized')
    no_of_pages = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=100, default="en")
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return self.title
