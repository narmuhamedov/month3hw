from django.urls import path, include
from . import views

urlpatterns = [
    path('books_lib/', views.shows_book_all, name ='book_lib_all'),
    path('book_lib/<int:id>/', views.book_info,name='book_info'),
    path('add-books/', views.add_book,name='add_book'),
]