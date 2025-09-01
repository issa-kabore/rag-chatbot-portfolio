import os
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

from src import logger
from src.config import FAISS_INDEX_PATH


logger.info("Starting the RAG portfolio processing script.")
# --- 1. Load the text document ---
DATA_DIR = Path("data")
MODEL_DIR = Path("model")
FILE_PATH = DATA_DIR / "portfolio.txt"

if not os.path.exists(FILE_PATH):
    logger.error(
        f"The file {FILE_PATH} was not found. Please ensure it is in the project directory."
    )
    raise FileNotFoundError(
        f"The file {FILE_PATH} was not found. Please ensure it is in the project directory."
    )


try:
    # Use TextLoader to read the file content with UTF-8 encoding.
    loader = TextLoader(FILE_PATH, encoding="utf-8")
    documents = loader.load()
    logger.info("Document loaded successfully.")
except Exception as e:
    raise IOError(f"Failed to load the document: {e}")

# --- 2. Split the document into smaller chunks ---
# A text splitter breaks down the large document into manageable chunks.
# This improves RAG accuracy by ensuring the LLM receives highly relevant context.
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Each chunk will have a maximum of 500 characters.
    chunk_overlap=50,  # Chunks will overlap by 50 characters to maintain context.
)
docs = text_splitter.split_documents(documents)
logger.info(f"Document split into {len(docs)} chunks.")

# --- 3. Create embeddings for each chunk ---
# Embeddings are numerical representations of text, capturing its semantic meaning.
# We use a Sentence-Transformers model, which is highly efficient.
try:
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/distiluse-base-multilingual-cased-v1"
    )
    logger.info("Embeddings model loaded.")
except Exception as e:
    logger.error(f"Failed to load the embeddings model: {e}")
    raise RuntimeError(f"Failed to load the embeddings model: {e}")

# --- 4. Create and save the FAISS vector database ---
# FAISS is a library for efficient similarity search and clustering of dense vectors.
# It acts as our vector database.
try:
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(FAISS_INDEX_PATH)
    logger.info("FAISS vector database created and saved successfully.")
except Exception as e:
    logger.error(f"Failed to create or save the FAISS index: {e}")
    raise RuntimeError(f"Failed to create or save the FAISS index: {e}")
