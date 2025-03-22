from src.fetch_api_data import fetch_api_data
from src.data_processing import process_api_data, generate_embeddings
from src.vector_db import initialize_pinecone, create_pinecone_index, store_embeddings, retrieve_sample_embeddings

def main():
    print("Fetching API data...")
    data = fetch_api_data()

    if data is None:
        print("API data fetch failed. Exiting.")
        return

    print("Processing data...")
    df = process_api_data(data)

    print("Generating embeddings...")
    embeddings = generate_embeddings(df)

    print("Initializing Pinecone...")
    pc = initialize_pinecone()
    create_pinecone_index(pc)

    print("Storing embeddings in Pinecone...")
    metadata = df.to_dict(orient="records")
    store_embeddings(pc, embeddings, metadata)

    print("Retrieving sample embeddings from Pinecone...")
    top_k_results = retrieve_sample_embeddings(pc)

    print("\nSample query results:")
    for result in top_k_results:
        print(f"ID: {result['id']}, Score: {result['score']}, Metadata: {result['metadata']}")

if __name__ == "__main__":
    main()
