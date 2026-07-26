import os
from dotenv import load_dotenv
from google import genai

from src.rag.retriever import Retriever

load_dotenv()


class RAGEngine:

    def __init__(self):
        self.retriever = Retriever()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")

        self.client = genai.Client(
            api_key=api_key
        )


    def ask(self, question):

        # 1. Get documents from vector database
        context = self.retriever.retrieve(question)

        prompt = f"""
You are an AI research assistant.

Use the following documents to answer.

Documents:
{context}

Question:
{question}

Answer clearly.
"""


        response = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )


        return response.text