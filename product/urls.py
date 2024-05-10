from django.urls import path

from product.views.product_view import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
    product_gte_stock_list,
    product_lte_stock_list
    
)
from product.views.category_view import (
    category_list,
    category_create,
    category_delete,
    category_update,
    category_detail,
    
)
urlpatterns = [
    #   URLs de los productos
    path(route='', view=product_list, name='product_list'),
    path(route='create/',view=product_create, name='product_create'),
    path(route='<int:id>/',view=product_detail,name="product_detail"),
    path(route='<int:id>/update/',view=product_update,name="product_update"),
    path(route='<int:id>/delete/',view=product_delete,name="product_delete"),
    path(route='category/', view=category_list, name='category_list'),
    path(route='stock/gte/', view=product_gte_stock_list, name='product_gte_stock_list'),
    path(route='stock/lte/', view=product_lte_stock_list, name='product_lte_stock_list'),

    #   URLs de las categorias
   # URL para listar todas las categorías
    path(route='category/<int:id>/', view=category_list, name='category_list'),
    # URL para crear una nueva categoría
    path(route='category/create/', view=category_create, name='category_create'),

    # URL para actualizar una categoría específica
    path(route='category/<int:id>/update/',view=category_update, name="category_update"),

    # URL para eliminar una categoría específica
    path(route='category/<int:id>/delete/', view=category_delete, name='category_delete'),

    # URL para ver los detalles de una categoría específica
    path(route='<int:id>/detail/',view=category_detail,name="category_detail"),



]