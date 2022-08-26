
from django.shortcuts import render,redirect
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


def update(request,  id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        save_update = BookForms(request.POST, request.FILES, instance=book_id)
        if save_update.is_valid():
            save_update.save()
            return redirect('/')
    else:
        save_update=BookForms(instance=book_id)
        
    context ={
        'form':save_update,
    }
    return render(request ,'pages/update.html',context)



def delete(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    
    return render(request,'pages/delete.html')