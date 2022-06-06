from django.db import models

# Create your models here.
class Book(models.Model):
    srno=models.IntegerField(primary_key=True)
    bookname = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()
    quantity=models.IntegerField()
 
    def __str__(self):
        return f"{self.srno},{self.bookname},{self.author},{self.isbn},{self.category},{self.quantity}"
        
