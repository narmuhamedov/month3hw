from django.urls import path, include
from . import views

app_name ='books'


urlpatterns = [
    path('books_lib/', views.shows_book_all, name ='book_lib_all'),
    path('book_lib/<int:id>/', views.book_info,name='book_info'),
    path('book_lib/<int:id>/update/', views.book_update,name='book_update'),
    path('book_lib/<int:id>/delete/', views.book_delete,name='book_delete'),
    path('add-books/', views.add_book,name='add_book'),

]