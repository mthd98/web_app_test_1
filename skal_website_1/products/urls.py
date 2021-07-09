from  django.urls import  path
from .views import show_products_page,show_product_detail_page

urlpatterns = [
    path('products/', show_products_page,name='products-page'),
    path('products/<int:id>', show_product_detail_page,name='product-detail-page'),
   
]