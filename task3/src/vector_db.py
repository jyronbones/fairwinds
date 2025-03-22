import pinecone
from sentence_transformers import SentenceTransformer
from src.config import PINECONE_API_KEY, PINECONE_ENV, PINECONE_INDEX, CHUNK_SIZE


def initialize_pinecone():
    pc = pinecone.Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
    print(f"Pinecone initialized in environment {PINECONE_ENV}.")
    return pc


def create_pinecone_index(pc, index_name=PINECONE_INDEX, dimension=768):
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric="cosine",
            spec=pinecone.ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
        print(f"Created index: {index_name}")
    else:
        print(f"Index {index_name} already exists")


def store_embeddings(pc, embeddings, metadata, index_name=PINECONE_INDEX):
    index = pc.Index(index_name)

    num_chunks = (len(embeddings) + CHUNK_SIZE - 1) // CHUNK_SIZE

    for chunk_idx in range(num_chunks):
        start = chunk_idx * CHUNK_SIZE
        end = min(start + CHUNK_SIZE, len(embeddings))

        vectors = [
            {
                "id": str(start + i),
                "values": embeddings[start + i].tolist(),
                "metadata": {"time": metadata[start + i]["time"]}
            }
            for i in range(end - start)
        ]

        index.upsert(vectors=vectors, namespace="weather-namespace")
        print(f"Inserted {len(vectors)} vectors into Pinecone.")


def retrieve_sample_embeddings(pc, index_name=PINECONE_INDEX, top_k=5):
    index = pc.Index(index_name)

    # Example query string for specific date and time
    query_string = "2025-03-25T09:00"

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query_string])[0]

    query_embedding_list = query_embedding.tolist()

    result = index.query(vector=query_embedding_list, top_k=top_k, include_values=True, include_metadata=True,
                         namespace="weather-namespace")

    return result['matches']



def query_pinecone(pc, index_name, query_embedding, top_k=5):
    index = pc.Index(index_name)

    response = index.query(
        vector=query_embedding.tolist(),
        top_k=top_k,
        include_values=True,
        include_metadata=True,
        namespace="weather-namespace"
    )

    return response['matches']
