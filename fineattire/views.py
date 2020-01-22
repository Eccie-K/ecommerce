from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpRequest,HttpResponse,Http404
from .models import Product
from cart import views


# Create your views here.
def home(request):

    return  render(request, 'home.html')



class Shop(ListView):
    model = Product
    
    
    template_name = 'products.html'

    