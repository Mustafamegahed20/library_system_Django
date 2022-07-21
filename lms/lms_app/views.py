from django.shortcuts import render
from .models import *
from .forms import BookForm,CategoryForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST,request.FILES)
        Cat=CategoryForm(request.POST)
        if Cat.is_valid():
            Cat.save()
        if add_book.is_valid():
            add_book.save()
    
    context={
        'Category':Category.objects.all(),
        'books':Book.objects.all(),
        'form':BookForm(),
        'Catform':CategoryForm()
    }    
    return render(request,'pages/index.html',context) 

def books(request): 
    context={
        'Category':Category.objects.all(),
        'books':Book.objects.all(),
    }     
    return render(request,'pages/books.html',context) 

