from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import Q
from cart.forms import CartAddProductForm
from .models import Category, Product
# Страница с товарами



def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    query = request.GET.get("query")


    if query:
        products = Product.objects.filter(Q(name__icontains=query))

        return render(request, 'product/list.html', {
            'products': products,

        })

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })
# Страница товара
def ProductDetail(request, id, slug):

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'product/detail.html', {'product': product})

# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form})