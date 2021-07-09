from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your views here.

def show_products_page(request,*args,**kwargs):
    objects=Product.objects.all()
    context={'objs':objects}
    return render(request,'products_page.html',context)

def show_product_detail_page(request,id=id,*args,**kwargs):


    object=get_object_or_404(Product,id=id)
    context={'obj':object}
    return render(request,'product_detail.html',context)