from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

import requests
from .models import Product

# Create your views here.


def load_products(request):
    if Product.objects.exists():
        return redirect(reverse("product_list"))

    prod_endpoint = "https://fakestoreapi.com/products/"
    resp = requests.get(prod_endpoint)
    products = []
    for item in resp.json():
        prod = Product(
            title=item["title"],
            image_url=item["image"],
            description=item["description"],
            price=item["price"],
        )
        products.append(prod)
    Product.objects.bulk_create(products)
    return redirect(reverse("product_list"))


def product_list(request):
    context = {"products": Product.objects.all()}
    return render(request, "products/product-list.html", context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product": product}

    if "recently_viewed" in request.session:
        recently_viewed = request.session["recently_viewed"]
        if product.id in recently_viewed:
            recently_viewed.remove(product.id)
        context["recently_viewed"] = sorted(
            Product.objects.filter(id__in=recently_viewed),
            key=lambda prod: recently_viewed.index(prod.id),
        )
        recently_viewed.insert(0, product.id)
        if len(recently_viewed) > 5:
            recently_viewed.pop()
    else:
        request.session["recently_viewed"] = [product.id]

    request.session.modified = True

    return render(request, "products/single-prod.html", context)
