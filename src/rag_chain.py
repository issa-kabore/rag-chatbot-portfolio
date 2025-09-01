from src import logger
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import *


def setup_rag_chain():
    """Initializes and returns the RetrievalQA chain."""
    try:
        if not GOOGLE_API_KEY:
            logger.error("GOOGLE_API_KEY is not set in the environment variables.")
            return None

        logger.info("Loading embeddings model...")
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDINGS_MODEL_NAME)
        logger.info("Embeddings model loaded successfully.")

        logger.info("Loading FAISS vector database...")
        db = FAISS.load_local(
            FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True
        )
        logger.info("FAISS vector database loaded successfully.")

        logger.info("Initializing Google Gemini LLM...")
        llm = ChatGoogleGenerativeAI(model=LLM_MODEL_NAME, temperature=LLM_TEMPERATURE)

        logger.info("Google Gemini LLM initialized.")

        prompt_template = """Tu es un assistant utile. Réponds à la question de l'utilisateur en te basant uniquement sur le contexte fourni. Synthétise la réponse et ne la copie pas directement. Si tu ne connais pas la réponse, dis simplement que tu ne sais pas, ne cherche pas à inventer une réponse.
        Contexte:
        {context}
        Question:
        {question}
        """
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(),
            chain_type_kwargs={"prompt": PROMPT},
            return_source_documents=True,
        )
        logger.info("RAG chain created successfully.")
        return qa_chain

    except Exception as e:
        logger.error(f"Error during RAG setup: {e}")
        return None
