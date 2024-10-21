from products.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get("cart_session")

        if not cart:
            cart = self.session["cart_session"] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        self.cart[product_id] = int(product_qty)
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def __contains__(self, product):
        return str(product.id) in self.cart

    def __iter__(self):
        product_ids = self.cart.keys()

        for prod in Product.objects.filter(id__in=product_ids):
            yield prod

    def get_quants(self):
        quantities = self.cart
        return quantities
