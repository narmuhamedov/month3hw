from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from . import models, forms
from django.views import generic

# class all

class BooksListView(generic.ListView):
    template_name = 'category_book.html'
    queryset = models.BookCategory.objects.all()

    def get_queryset(self):
        return models.BookCategory.objects.all()

# def shows_book_all(request):
#     shows = models.BookCategory.objects.all()
#     return render(request, 'category_book.html', {'shows': shows})


# class id
class BookDetailView(generic.DetailView):
    template_name = 'book_info.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.BookCategory, id = book_id)



# def book_info(request, id):
#     show = get_object_or_404(models.BookCategory, id=id)
#     return render(request, 'book_info.html',{'show':show})

# class add

class BookCreateView(generic.CreateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    queryset = models.BookCategory.objects.all()
    success_url = "/books_lib/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form = form)


# def add_book(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse('Book created')
#             return redirect(reverse("books:book_lib_all"))
#     else:
#         form = forms.BookForm()
#     return render(request, 'add_book.html', {'form': form})

# class update

class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/books_lib/"

    def get_object(self, *kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.BookCategory, id = books_id)
    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)


# def book_update(request, id):
#      book_obj = get_object_or_404(models.BookCategory, id = id)
#      if request.method == 'POST':
#          form = forms.BookForm(instance=book_obj, data=request.POST)
#          if form.is_valid():
#              form.save()
#              # return HttpResponse('Books Update ')
#              return redirect(reverse("books:book_lib_all"))
#      else:
#          form = forms.BookForm(instance=book_obj)
#      return render(request, 'book_update.html', {'form':form,'object': book_obj })


#class delete

class BookDeleteView(generic.DeleteView):
    template_name = "confirm_delete_book.html"
    success_url = "/books_lib/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.BookCategory,id = book_id)




# def book_delete(request, id):
#      book_obj = get_object_or_404(models.BookCategory, id = id)
#      book_obj.delete()
#      # return HttpResponse('Book Deleted')
#      return redirect(reverse("books:book_lib_all"))