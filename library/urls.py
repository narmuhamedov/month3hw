from django.urls import path, include
from . import views

app_name ='books'


urlpatterns = [
    path('books_lib/', views.BooksListView.as_view(), name ='book_lib_all'),
    path('book_lib/<int:id>/', views.BookDetailView.as_view(),name='book_info'),
    path('book_lib/<int:id>/update/', views.BookUpdateView.as_view(),name='book_update'),
    path('book_lib/<int:id>/delete/', views.BookDeleteView.as_view(),name='book_delete'),
    path('add-books/', views.BookCreateView.as_view(),name='add_book'),
]