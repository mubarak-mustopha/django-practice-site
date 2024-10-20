class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get("cart_session")

        if not cart:
            cart = self.session["cart_session"] = {}

        self.cart = cart
