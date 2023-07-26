from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

class BookSale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    sale_date = models.DateField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.book.title} - {self.sale_date} - Quantity: {self.quantity}"