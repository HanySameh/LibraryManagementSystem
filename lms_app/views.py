from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def index(request):
    if request.method == 'POST':
        add_book = BookForms(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
        'books': Book.objects.all(),
        'categores': Category.objects.all(),
        'form': BookForms(),
        'cat_form': CategoryForm()
    }
    return render(request, 'pages/index.html', context)


def books(request):
    context = {
        'books': Book.objects.all(),
        'categores': Category.objects.all(),
        'cat_form': CategoryForm()

    }
    return render(request, 'pages/books.html', context)
