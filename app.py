from flask import Flask, render_template, abort, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "change-this-later-to-a-random-secret"

PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 2500, "description": "Comfortable headphones with clear sound."},
    {"id": 2, "name": "Smart Watch", "price": 4500, "description": "Track your steps and notifications."},
    {"id": 3, "name": "Backpack", "price": 1800, "description": "Strong and spacious bag for everyday use."},
    {"id": 4, "name": "Water Bottle", "price": 600, "description": "Keeps your drink cold for 12 hours."},
]


def find_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


@app.route("/")
def home():
    cart_count = sum(session.get("cart", {}).values())
    return render_template("index.html", products=PRODUCTS, cart_count=cart_count)


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = find_product(product_id)
    if product is None:
        abort(404)
    cart_count = sum(session.get("cart", {}).values())
    return render_template("product.html", product=product, cart_count=cart_count)


@app.route("/add-to-cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    if find_product(product_id) is None:
        abort(404)
    cart = session.get("cart", {})
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    session["cart"] = cart
    return redirect(url_for("cart_page"))


@app.route("/cart")
def cart_page():
    cart = session.get("cart", {})
    items = []
    total = 0
    for key, quantity in cart.items():
        product = find_product(int(key))
        if product:
            subtotal = product["price"] * quantity
            total += subtotal
            items.append({"product": product, "quantity": quantity, "subtotal": subtotal})
    cart_count = sum(cart.values())
    return render_template("cart.html", items=items, total=total, cart_count=cart_count)


if __name__ == "__main__":
    app.run(debug=True)