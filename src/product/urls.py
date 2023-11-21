from django.urls import path
from product.views import Home, AddProduct, UpdateProduct, DeleteProduct, DetailProduct

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('addProduct', AddProduct.as_view(), name='addProduct'),
    path('detailsProduct/<int:produto_id>',DetailProduct.as_view(), name='details'),
    path('updateProduct/<int:produto_id>',UpdateProduct.as_view(), name='updateProduct'),
    path('deleteProduct/<int:produto_id>', DeleteProduct.as_view(), name='deleteProduct')
]