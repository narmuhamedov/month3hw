from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from . import models, forms


def shows_book_all(request):
    shows = models.BookCategory.objects.all()
    return render(request, 'category_book.html', {'shows': shows})

def book_info(request, id):
    show = get_object_or_404(models.BookCategory, id=id)
    return render(request, 'book_info.html',{'show':show})


def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Book created')
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_update(request, id):
     book_obj = get_object_or_404(models.BookCategory, id = id)
     if request.method == 'POST':
         form = forms.BookForm(instance=book_obj, data=request.POST)
         if form.is_valid():
             form.save()
             # return HttpResponse('Books Update ')
             return redirect(reverse("books:book_lib_all"))
     else:
         form = forms.BookForm(instance=book_obj)
     return render(request, 'book_update.html', {'form':form,'object': book_obj })

def book_delete(request, id):
     book_obj = get_object_or_404(models.BookCategory, id = id)
     book_obj.delete()
     return HttpResponse('Book Deleted')
