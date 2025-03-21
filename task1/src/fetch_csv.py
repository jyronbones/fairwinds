import pandas as pd
import requests
from io import StringIO
from src.config import CSV_URL

def fetch_csv_data():
    response = requests.get(CSV_URL)
    response.raise_for_status()
    csv_data = StringIO(response.text)
    return csv_data

def convert_to_dataframe(csv_data):
    df = pd.read_csv(csv_data)
    return df