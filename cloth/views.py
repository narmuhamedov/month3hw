from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms

#тег для списка всей одежды
class ProductCLView(ListView):
    queryset = models.ProductCL.objects.filter().order_by('-id')
    template_name = 'productscl.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by('-id')

#тег для мужчин
class Product_manClView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='man').order_by('-id')
    template_name = 'productscl_man.html'
    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='man').order_by('-id')
#тег для женщин
class Product_womanClView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='woman').order_by('-id')
    template_name = 'productscl_woman.html'
    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='woman').order_by('-id')

#тег для детей
class Product_childsClView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='childs').order_by('-id')
    template_name = 'productscl_childs.html'
    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='childs').order_by('-id')

#тег универсальной одежды
class Product_unisexClView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='unisex').order_by('-id')
    template_name = 'productscl_unisex.html'
    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='unisex').order_by('-id')





class ProductCLDetailView(DetailView):
    template_name = 'productscl_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.ProductCL, id=product_id)


# для Order
class OrderCreateView(CreateView):
    template_name = "add_ordercl.html"
    form_class = forms.OrderForm
    success_url = "/productscl/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)