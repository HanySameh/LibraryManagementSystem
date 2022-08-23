from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    context ={
        'books':Book.objects.all(),
        'categores':Category.objects.all(), 
    }
    return render(request, 'pages/index.html',context=context)


def books(request):
    return render(request, 'pages/books.html')


