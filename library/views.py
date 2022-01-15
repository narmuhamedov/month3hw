from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
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