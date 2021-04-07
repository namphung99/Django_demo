from django.shortcuts import render,HttpResponse,redirect
from .models import Products, Account


from django.views import View

from django.contrib.auth import authenticate,login



# Create your views here.

# class IndexClass(View):
#     def get(self,request):
#          return HttpResponse('<h1>Login</h1>')


class LoginClass(View):
    def get(self,request):
        return render(request,'login/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        my_user = authenticate(username= username, password=password)
        Acc = {'Account' : Account.objects.all().order_by("username")}
       
        if my_user is None:
            return HttpResponse('<script>alert("Sai thông tin tài khoản, quay về trang trước",window.location.href = "http://127.0.0.1:8000/") </script>')
            # return render(request,'login/loginFail.html',Acc)
        
        login(request,my_user)
        Data = {'Products' : Products.objects.all().order_by("id")}
        return render(request,'products/home.html',Data)

class RegisterClass(View):
    def get(self,request):
        return render(request,'register/register.html')
def list(request):
    Data = {'Products' : Products.objects.all().order_by("id")}
    return render(request,'products/home.html',Data)
