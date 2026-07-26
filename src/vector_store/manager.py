import chromadb
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):

        # Create/Open ChromaDB database
        self.client = chromadb.PersistentClient(
        path="data/vector_db"
        )

        # Create collection
        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        # Load embedding model
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def add_chunks(self, doc_id, chunks):

        ids = []
        documents = []
        metadatas = []
        embeddings = []

        for chunk in chunks:

            ids.append(f"{doc_id}_{chunk['chunk_id']}")

            documents.append(chunk["text"])

            metadatas.append({
                "doc_id": doc_id,
                "page_number": chunk["page_number"]
            })

            embedding = self.model.encode(
                chunk["text"]
            ).tolist()

            embeddings.append(embedding)

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )


    def search(self, query, top_k=5):

        query_embedding = self.model.encode(
            query
        ).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results
