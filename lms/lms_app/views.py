from django.shortcuts import get_object_or_404, redirect, render
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

def update(request,id):
    book_id=Book.objects.get(id=id)
    if request.method == 'POST':
        book_save=BookForm(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect("/")
    else:
        book_save=BookForm(instance=book_id)
    
    context ={
        'form':book_save,
    }
    
    return render(request,'pages/update.html',context)

def delete(request,id):
    book_delete = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')
    