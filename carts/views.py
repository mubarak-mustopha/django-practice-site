from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from products.models import Product
from .carts import Cart


# Create your views here.
def cart_summary(request):
    return render(request, "carts/cart_summary.html", {})


def cart_add(request):
    cart = Cart(request)
    data = request.POST
    print(f"----POST DATA-----\n{request.POST}")
    print(f"----REQUEST METHOD-----\n{request.method}")
    if data.get("action") == "post":
        product_id = int(data.get("product_id"))
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product)

        # return response
        return JsonResponse({"Product Name": product.name})


def cart_delete(request):
    pass


def cart_update(request):
    pass
