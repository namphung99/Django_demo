from django.contrib import admin
from .models import Product
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','price']
admin.site.register(Product, PostAdmin)