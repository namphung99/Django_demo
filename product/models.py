from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=25)
    image = models.CharField(max_length= 100)
    author = models.CharField(max_length= 100)
    quantity = models.IntegerField

    def __str__(self):
        return self.title