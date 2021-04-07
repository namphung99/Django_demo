from django.urls import path
from . import views
from .views import LoginClass,RegisterClass

urlpatterns = [
    path('',LoginClass.as_view(), name ='login'),
    path('register/',RegisterClass.as_view(), name ='register'),
    path('products/',views.list)
]