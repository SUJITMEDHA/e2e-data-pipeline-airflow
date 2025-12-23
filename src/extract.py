import requests

def extract_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
