# importing the requests library
import requests

# api-endpoint
BASE_URL = 'https://fakestoreapi.com'

# query parameter
query_params = {
    "limit": 3
}

response = requests.get(f"{BASE_URL}/products", params=query_params)
print(response.json())
print(response.status_code)

