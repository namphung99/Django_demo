from django.urls import path
from . import views
from .views import LoginClass

urlpatterns = [
    path('',LoginClass.as_view(), name ='login'),
    path('register/',views.register, name ='register'),
    path('products/',views.list)
]