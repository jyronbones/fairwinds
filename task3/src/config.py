import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV", "us-east-1")
PINECONE_INDEX = os.getenv("PINECONE_INDEX", "weather-index")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 100))
