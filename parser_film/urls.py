from django.urls import path, include
from . import views

app_name ='parse'

urlpatterns = [
    path('parser_film/', views.ParserFormView.as_view(), name ='parse_func'),
    path('parser_film_info/', views.ParserView.as_view(), name ='parse_view'),

]