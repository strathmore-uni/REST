from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#data for supercars
products = [
    {"name": "Ferrari LaFerrari", "description": "A hybrid supercar with a V12 engine.", "price": 1000000},
    {"name": "Lamborghini Aventador", "description": "A powerful V12 supercar with stunning design.", "price": 400000},
    {"name": "McLaren P1", "description": "A hybrid supercar that combines performance and efficiency.", "price": 1200000},
    {"name": "Bugatti Chiron", "description": "One of the fastest production cars in the world.", "price": 3000000},
    {"name": "Porsche 918 Spyder", "description": "A plug-in hybrid supercar with exceptional performance.", "price": 850000},
    {"name": "Aston Martin Valkyrie", "description": "A hypercar with a naturally aspirated V12 engine.", "price": 3000000}
]

class Product(BaseModel):
    name: str
    description: str
    price: float

@app.get("/products")
def get_products():
    """Retrieve a list of all products as JSON."""
    return products

@app.post("/products", status_code=201)
def add_product(product: Product):
    """Accepts a JSON object to create a new product."""
    products.append(product.dict())
    return product.dict()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)