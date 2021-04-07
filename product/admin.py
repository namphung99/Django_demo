from django.contrib import admin
from .models import Products, Account, Fullname, Address, Customer
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']


admin.site.register(Products, PostAdmin)
admin.site.register(Fullname)
admin.site.register(Address)
admin.site.register(Customer)
