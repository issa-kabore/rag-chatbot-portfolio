import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- API and Model Configurations ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Hugging Face Embeddings model
EMBEDDINGS_MODEL_NAME = "sentence-transformers/distiluse-base-multilingual-cased-v1"

# LLM Configurations
LLM_MODEL_NAME = "gemini-1.5-flash"
LLM_TEMPERATURE = 0.4

# RAG specific configurations
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
FAISS_INDEX_PATH = "./data/faiss_portfolio_index"