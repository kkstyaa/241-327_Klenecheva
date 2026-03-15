from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.CharField(max_length=100, verbose_name="Author")
    published_date = models.DateField(verbose_name="Published date")
    is_available = models.BooleanField(default=True, verbose_name="Is available")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    
    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
