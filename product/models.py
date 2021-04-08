from django.db import models

# Create your models here.

# class Product(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.CharField(max_length=25)
#     image = models.CharField(max_length= 100)
#     author = models.CharField(max_length= 100)
#     quantity = models.IntegerField

#     def __str__(self):
#         return self.title

class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Fullname(models.Model):
    firstName = models.CharField(max_length=50)
    midName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

class Address(models.Model):
    street = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Customer(models.Model):
    Id = models.CharField(max_length=50)
    fullname = models.OneToOneField(
        Fullname,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    acc = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        # primary_key=True,
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        # primary_key=True,
    )
    contact =models.CharField(max_length=50)

class Comment(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Products(models.Model):
    title = models.CharField(max_length=100)
    name =  models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.FloatField()
    image = models.CharField(max_length= 100)
    author = models.CharField(max_length= 100)

    # def __str__(self):
    #     return self.title

class Item(models.Model):
    name = models.CharField(max_length=200)
    amountRemain = models.IntegerField(default=5)
    priceSale = models.FloatField()
    shopName = models.CharField(max_length=200)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)



class Cart(models.Model):
    quantity = models.IntegerField(default=0)
    total = models.FloatField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Shipment(models.Model):
    type = models.CharField(max_length= 100)
    cost = models.FloatField()

class Payment(models.Model):
    type = models.CharField(max_length= 100)
    total = models.FloatField()
    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
        # primary_key=True,
    )
    shipment = models.OneToOneField(
        Shipment,
        on_delete=models.CASCADE,
        # primary_key=True,
    )

class Order(models.Model):
    destination = models.CharField(max_length=200)
    dateCreate = models.DateTimeField('date Order')
    total = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipment = models.OneToOneField(
        Shipment,
        on_delete=models.CASCADE,
        primary_key=True,
    )