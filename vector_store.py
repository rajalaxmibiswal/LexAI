import chromadb
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.client = chromadb.Client()

        try:
            self.collection = self.client.get_collection(
                "legal_docs"
            )
        except:
            self.collection = self.client.create_collection(
                "legal_docs"
            )

    def add_documents(self, chunks):

        embeddings = self.model.encode(chunks).tolist()

        for i, chunk in enumerate(chunks):

            self.collection.add(
                ids=[f"doc_{i}"],
                documents=[chunk],
                embeddings=[embeddings[i]]
            )

    def search(self, query):

        embedding = self.model.encode(
            [query]
        ).tolist()

        results = self.collection.query(
            query_embeddings=embedding,
            n_results=5
        )

        return results["documents"][0]