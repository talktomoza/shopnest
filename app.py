from flask import Flask, render_template, abort

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 2500, "description": "Comfortable headphones with clear sound."},
    {"id": 2, "name": "Smart Watch", "price": 4500, "description": "Track your steps and notifications."},
    {"id": 3, "name": "Backpack", "price": 1800, "description": "Strong and spacious bag for everyday use."},
    {"id": 4, "name": "Water Bottle", "price": 600, "description": "Keeps your drink cold for 12 hours."},
]


@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return render_template("product.html", product=product)
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)