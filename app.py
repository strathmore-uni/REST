from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for supercars
products = [
    {"name": "Ferrari LaFerrari", "description": "A hybrid supercar with a V12 engine.", "price": 1000000},
    {"name": "Lamborghini Aventador", "description": "A powerful V12 supercar with stunning design.", "price": 400000},
    {"name": "McLaren P1", "description": "A hybrid supercar that combines performance and efficiency.", "price": 1200000},
    {"name": "Bugatti Chiron", "description": "One of the fastest production cars in the world.", "price": 3000000},
    {"name": "Porsche 918 Spyder", "description": "A plug-in hybrid supercar with exceptional performance.", "price": 850000},
    {"name": "Aston Martin Valkyrie", "description": "A hypercar with a naturally aspirated V12 engine.", "price": 3000000}
]

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve a list of all products as JSON."""
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    """Accepts a JSON object to create a new product."""
    product_data = request.json
    
    # Validate all the incoming data 
    if not product_data or not all(key in product_data for key in ('name', 'description', 'price')):
        return jsonify({"error": "Missing data or invalid input"}), 400
    
    # Ensure price is a valid number
    if not isinstance(product_data['price'], (int, float)) or product_data['price'] < 0:
        return jsonify({"error": "Price must be a positive number"}), 400

    products.append(product_data)
    return jsonify(product_data), 201

if __name__ == '__main__':
    app.run(debug=True)