import chromadb
from sentence_transformers import SentenceTransformer


class Retriever:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vector_db"
        )

        self.collection = self.client.get_or_create_collection(
             name="documents"
        )

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def retrieve(self, question):

        # Convert question into embedding
        embedding = self.model.encode(question).tolist()


        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=5
        )


        documents = results["documents"][0]


        if not documents:
            return "No documents available"


        context = "\n\n".join(documents)

        return context