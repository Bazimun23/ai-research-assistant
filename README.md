# AI Research Assistant

## Overview

AI Research Assistant is a Retrieval-Augmented Generation (RAG) application built with FastAPI. It allows users to upload PDF documents, stores them in a vector database, and answers questions based on the uploaded documents using Google Gemini.

## Features

- Upload PDF documents
- Extract text from PDFs
- Split text into chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in ChromaDB
- Retrieve relevant document chunks
- Answer questions using Gemini
- List uploaded documents
- Delete uploaded documents

## Technologies Used

- Python
- FastAPI
- Google Gemini API
- ChromaDB
- Sentence Transformers
- PyMuPDF
- SQLite

## Project Structure

```
ai-research-assistant/
│── config/
│── data/
│── routes/
│── screenshots/
│── src/
│── main.py
│── requirements.txt
│── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Bazimun23/ai-research-assistant.git
```

2. Navigate to the project

```bash
cd ai-research-assistant
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Create a `.env` file and add your Gemini API key.

Example:

```
GEMINI_API_KEY=your_api_key
```

7. Run the application

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

- POST `/documents/upload`
- GET `/documents/`
- DELETE `/documents/{doc_id}`
- POST `/rag/ask`

## Screenshots

Screenshots are available in the `screenshots` folder.

## Author

**Bazimun Shaik**
