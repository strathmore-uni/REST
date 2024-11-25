# REST
# Supercar API

This project is a simple REST API built with Flask to manage a collection of supercars. It provides endpoints to add new products and retrieve a list of all products.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setting Up the Environment](#setting-up-the-environment)
- [Running the API Server](#running-the-api-server)
- [Testing the API Endpoints](#testing-the-api-endpoints)
  - [Manual Testing with cURL](#manual-testing-with-curl)
  - [Testing with the Provided Python Script](#testing-with-the-provided-python-script)

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or later
- pip (Python package installer)

## Setting Up the Environment

1. **Clone the Repository**
   If you haven't already, clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
Create a Virtual Environment (Optional but Recommended) It's a good practice to use a virtual environment for Python projects. You can create one using the following commands:
bash


python -m venv venv
Activate the Virtual Environment
On Windows:
bash


venv\Scripts\activate
On macOS/Linux:
bash


source venv/bin/activate
Install Required Packages Install the required packages using pip:
bash


pip install Flask requests
Running the API Server
Run the API Start the Flask API server by running the app.py file:
bash


python app.py
Access the API The API server will be running locally at http://127.0.0.1:5000. You can access the endpoints using this URL "http://127.0.0.1:5000/products"
Testing the API Endpoints
Manual Testing with cURL
You can test the API endpoints manually using cURL. Here are examples of how to interact with the API.
Add a New Product Use the following command to add a new product:
bash


curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{"name": "Koenigsegg Jesko", "description": "A hypercar with extreme performance.", "price": 2800000}'
Retrieve All Products Use the following command to retrieve the list of products:
bash


curl -X GET http://127.0.0.1:5000/products
Testing with the Provided Python Script
Run the Client Script The client.py script is provided to interact with the API easily. To run it, make sure your Flask server is running, and then execute:
bash


python client.py
Observe the Output The script will add two products and then retrieve and print the list of all products. You should see output confirming the successful addition of the products and a list of all products currently stored in the API.
Conclusion
You now have a fully functional REST API for managing supercars! Feel free to modify the code and add more functionality as needed. If you have any questions or feedback, please reach out.
javascript



## File Structure
Make sure to place this `README.md` file in the root directory of your project, alongside `app.py` and `client.py`. This will provide clear instructions for anyone who wants to set up and test your API. If you have any further modifications or additional features you'd like to document, feel free to ask!