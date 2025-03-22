import pandas as pd
from sentence_transformers import SentenceTransformer
from src.config import CHUNK_SIZE


def process_api_data(data):
    times = data['hourly']['time']
    temperatures = data['hourly']['temperature_2m']

    df = pd.DataFrame({'time': times, 'temperature_2m': temperatures})
    return df


def chunk_dataframe(df, chunk_size=CHUNK_SIZE):
    return [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]


def generate_embeddings(df_chunk):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    embeddings = model.encode(df_chunk['time'].tolist(), batch_size=CHUNK_SIZE, show_progress_bar=True)
    return embeddings
