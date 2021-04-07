from django.shortcuts import render
from .models import Products
# Create your views here.

def list(request):
    Data = {'Products' : Products.objects.all().order_by("id")}
    return render(request,'products/home.html',Data)
