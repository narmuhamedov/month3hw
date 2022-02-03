from django.urls import path
from . import views

app_name = 'productcl'
urlpatterns = [
    path('productscl/', views.ProductCLView.as_view(), name = 'prodcl_list'),
    path('productscl_man/', views.Product_manClView.as_view(), name = 'prodclman_list'),
    path('productscl_woman/', views.Product_womanClView.as_view(), name = 'prodclwoman_list'),
    path('productscl_childs/', views.Product_childsClView.as_view(), name = 'prodclchilds_list'),
    path('productscl_unisex/', views.Product_unisexClView.as_view(), name = 'prodclunisex_list'),

    path("add-order3/", views.OrderCreateView.as_view(), name="order_create"),
    path('productscl/<int:id>/', views.ProductCLDetailView.as_view(), name='prodcl_detail'),
]
