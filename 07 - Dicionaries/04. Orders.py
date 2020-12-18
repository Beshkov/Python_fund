product_data = input()

products = {}


while product_data != "buy":
    product, price, quantity = product_data.split()

    if product not in products:
        products[product] = {}
        products[product]["price"] = float(price)
        products[product]["quantity"] = int(quantity)
    else:
        products[product]["price"] = float(price)
        products[product]["quantity"] += int(quantity)

    product_data = input()

for item, item_info in products.items():
    total_item_cost = item_info["price"] * item_info["quantity"]
    print(f"{item} -> {total_item_cost:.2f}")