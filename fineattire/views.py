from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,Http404

# Create your views here.
def home(request):
    return render(request, 'home.html')

