import requests
from src.config import API_URL


def fetch_api_data():
    response = requests.get(API_URL)
    return response.json()