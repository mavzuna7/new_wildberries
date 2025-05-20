from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 7)  # показываем 7 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj": page_obj
    }
    return render(request, "app/index.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = []
    categories.append(product.category)
    cur_category = product.category
    while cur_category.parent:
        categories.append(cur_category.parent)
        cur_category = cur_category.parent
    categories.reverse()
    context = {"product": product, "categories": categories}
    return render(request, "app/product_details.html", context)

