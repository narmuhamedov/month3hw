from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.

def book_blog(request):
    index = models.Book.objects.all()
    return render(request, 'book_update.html', {'index':index})