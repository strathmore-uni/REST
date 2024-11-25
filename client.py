import requests

BASE_URL = 'http://127.0.0.1:5000/products'

def add_product(name, description, price):
    """Add a new product to the API."""
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }
    try:
        response = requests.post(BASE_URL, json=product_data)
        
        if response.status_code == 201:
            print("Successfully added product:", response.json())
        elif response.status_code == 400:
            print("Failed to add product: Bad Request -", response.json().get("error"))
        else:
            print("Failed to add product:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred while trying to add the product:", e)

def get_products():
    """Retrieve and print the list of all products from the API."""
    try:
        response = requests.get(BASE_URL)
        
        if response.status_code == 200:
            products = response.json()
            print("Products:")
            for product in products:
                print(f"Name: {product['name']}, Description: {product['description']}, Price: ${product['price']}")
        else:
            print("Failed to retrieve products:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred while trying to retrieve products:", e)

# Example interaction with the API
if __name__ == '__main__':
    # Adding any new products
    add_product('Koenigsegg Jesko', 'A hypercar with extreme performance.', 2800000)
    add_product('Porsche 911 GT3', 'A high-performance sports car.', 200000)
    
    # Retrieve and print all products well
    get_products()