# Imports necesarios
from django.shortcuts import redirect, render
from product.models import Category
from product.repositories.product import ProductRepository

# Crear una instancia del repositorio de productos
repo = ProductRepository()

# Vista para mostrar la lista de productos
def product_list(request):
    # Obtener todos los productos del repositorio
    productos = repo.get_all()
    return render(
        request,
        'products/list.html',
        dict(
            products=productos
        )
    )

# Vista para mostrar los detalles de un producto específico
def product_detail(request, id):
    # Obtener el producto con el ID proporcionado del repositorio
    producto = repo.get_by_id(id=id)
    return render(
        request,
        'products/detail.html',
        {"product":producto}
    )

# Vista para eliminar un producto
def product_delete(request, id):
    # Obtener el producto con el ID proporcionado del repositorio
    producto = repo.get_by_id(id=id)
    # Eliminar el producto del repositorio
    repo.delete(producto=producto)
    # Redirigir a la lista de productos después de eliminar
    return redirect('product_list')

# Vista para actualizar un producto
def product_update(request, id):
    # Obtener el producto con el ID proporcionado del repositorio
    product = repo.get_by_id(id=id)
    # Obtener todas las categorías disponibles
    categorias = Category.objects.all()
    if request.method == "POST":
        # Obtener los datos del formulario
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        # Obtener la categoría seleccionada por su ID
        category = Category.objects.get(id=id_category)

        # Actualizar el producto en el repositorio con los nuevos datos
        repo.update(
            producto=product,
            nombre=name,
            precio=price,
            descripcion=description,
            stock=stock,
            categoria=category
        )
        # Redirigir a la página de detalles del producto actualizado
        return redirect('product_detail', product.id)

    return render(
        request,
        'products/update.html',
        dict(
            categories=categorias,
            product=product
        )
    )

# Vista para crear un nuevo producto
def product_create(request): 
    if request.method == "POST":
        # Obtener los datos del formulario
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        # Obtener la categoría seleccionada por su ID
        category = Category.objects.get(id=id_category)

        # Crear un nuevo producto en el repositorio con los datos proporcionados
        producto_nuevo = repo.create(
            nombre=name,
            descripcion=description,
            precio=float(price),
            cantidades=stock,
            categoria=category
        )
        # Redirigir a la página de detalles del nuevo producto
        return redirect('product_detail', producto_nuevo.id)

    # Obtener todas las categorías disponibles para mostrar en el formulario
    categorias = Category.objects.all()
    return render (
        request,
        'products/create.html',
        dict(
            categories=categorias
        )
    )

# Vista de índice
def index_view(request):
    return render(
        request,
        'index/index.html'
    )

def product_gte_stock_list(request):
    min_stock = 0
    max_stock = float('inf')
    if request.method == "GET":
        min_stock_str = request.GET.get('min_stock', '0')
        max_stock_str = request.GET.get('max_stock', 'inf')
        print("Valor mínimo de stock recibido en GET:", min_stock_str)
        print("Valor máximo de stock recibido en GET:", max_stock_str)
        
        try:
            min_stock = int(min_stock_str)
            max_stock = int(max_stock_str)
        except ValueError:
            # En caso de que los valores ingresados no sean válidos, se mantienen los valores predeterminados
            pass
        
        # Obtener productos cuyo stock esté dentro del rango especificado
        productos = repo.get_product_stock_range(min_stock, max_stock)
    else:
        productos = repo.get_all()

    return render(  
        request,
        'products/list.html',
        dict(
            products=productos,
            min_stock=min_stock,
            max_stock=max_stock
        ) 
    )


def product_lte_stock_list(request):
    stock_threshold = 0  # Esto puede ser cualquier valor que desees
    productos = repo.get_product_lte_stock(stock_threshold)  
    return render(  
        request,
        'products/list.html',
        dict(
            products=productos  
        ) 
    )
