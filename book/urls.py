from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.book_blog, name='book_bloog'),

]
