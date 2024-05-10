from django.contrib import admin  # Importa el módulo de administración de Django
from django.urls import path, include  # Importa funciones para definir patrones de URL y para incluir otras URLconf

from product.views.product_view import index_view  # Importa la vista de índice desde la aplicación de productos

urlpatterns = [
    # URL para la página de inicio, que muestra el índice
    path('', index_view, name='index'),
    
    # URL para acceder al panel de administración de Django
    path('admin/', admin.site.urls),
    
    # URL para incluir las URLs de la aplicación de productos
    path('products/', include("product.urls")),
]
