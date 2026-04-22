import requests

def search_products(intent: dict):
    query = intent.get("category", "shoes")

    url = f"https://dummyjson.com/products/search?q={query}"
    res = requests.get(url)
    data = res.json()

    products = []

    for item in data.get("products", []):
        product = {
            "name": item["title"],
            "price": item["price"],
            "rating": item["rating"],
            "image": item["thumbnail"]
        }

        if intent["max_price"] and product["price"] > intent["max_price"]:
            continue

        products.append(product)

    return products
