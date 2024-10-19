from django.urls import path

from .views import load_products, product_list, product


urlpatterns = [
    path("load/", load_products, name="load_products"),
    path("", product_list, name="product_list"),
    path("<int:pk>/", product, name="product"),
]
