from django.urls import path
from . import views
from .views import LoginClass

urlpatterns = [
    path('',LoginClass.as_view(), name ='login'),
    path('products/',views.list)
]