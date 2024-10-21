from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from products.models import Product
from .carts import Cart


# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_prods = list(iter(cart))
    quantities = cart.get_quants()

    return render(
        request,
        "carts/cart_summary.html",
        {"cart_prods": cart_prods, "quantities": quantities},
    )


def cart_add(request):
    cart = Cart(request)
    data = request.POST
    if data.get("action") == "post":
        product_id = int(data.get("product_id"))
        product_qty = int(data.get("product_qty"))
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product, product_qty)

        # return response
        return JsonResponse({"qty": len(cart)})


def cart_delete(request):
    pass


def cart_update(request):
    pass
