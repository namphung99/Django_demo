from django.shortcuts import render
from .models import Product
# Create your views here.

def list(request):
    Data = {'Products' : Product.objects.all().order_by("id")}
    return render(request,'products/home.html',Data)
