from django.shortcuts import render, redirect, get_list_or_404
from django.core.paginator import Paginator
from .models import Product, Cart, CartItem


def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj  
    }
    return render(request, "app/index.html", context)

def product_details(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = []
    categories.append(product.category)
    cur_category = product.category
    while cur_category.parent:
        categories.append(cur_category.parent)
        cur_category = cur_category.parent
    categories.reverse()
    context = {"product": product, "categories": categories}
    return render(request, "app/product_details.html", context)

def add_to_cart(request, product_slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=product_slug)
        cart = request.session.get('cart', {})
        cart[str(product_slug)] = cart.get(str(product_slug), 0) + 1
        request.session['cart'] = cart
    return redirect('index')


def cart_view(request):
    cart = request.session.get('cart', {})  # Храним товары по slug
    cart_items = []
    total = 0

    for slug_key, quantity in cart.items():
        try:
            product = Product.objects.get(slug=slug_key)
            item_total = product.price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
            total += item_total
        except Product.DoesNotExist:
            continue

    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'app/cart.html', context)

def remove_from_cart(request, product_slug):
    cart = request.session.get('cart', {})
    if str(product_slug) in cart:
        del cart[str(product_slug)]
        request.session['cart'] = cart
    return redirect('cart')

