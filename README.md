# SRAXC (Self-Reflective AI eXpert Chatbot)

## 1\. Project Description

SRAXC is an AI-powered chatbot designed to answer questions about my professional portfolio, skills, and projects. It uses **Retrieval-Augmented Generation (RAG)** to provide accurate, personalized, and context-aware responses based on my personal documents.

**Try the app live here: : [SRAXC](https://rag-chatbot-portfolio-ulyvhd5kadvbnsvkmnghkp.streamlit.app/)**

The core technologies used in this project include:

  * **LangChain**: To orchestrate the RAG pipeline.
  * **Google Gemini**: A powerful LLM for text generation via API.
  * **Hugging Face**: For generating high-quality text embeddings.
  * **FAISS**: An efficient vector store for rapid similarity search.
  * **Streamlit**: To create an interactive and elegant web interface.

-----

## 2\. Project Architecture

The project is organized into a modular and clean structure for better maintainability.

```
/SRAXC
├── .env                          # Environment variables (API key - NOT tracked by Git)
├── .gitignore                    # Specifies files to be ignored by Git
├── data
│   ├── your_portfolio.txt        # Your source document containing portfolio details
│   └── faiss_portfolio_index/    # The FAISS vector database

├── src/                          # Source code for the application's logic
│   ├── __init__.py               # Project initialization and logging configuration
│   ├── config.py                 # Centralized configuration variables
│   └── rag_chain.py              # Logic to set up the RAG chain
├── rag_portfolio.py              # Script to create the FAISS index
├── streamlit_app.py              # Main Streamlit application script
└── requirements.txt              # Project dependencies
```

-----

## 3\. Installation and Setup

### Step 3.1: Clone the Repository and Set Up Virtual Environment

Clone this repository to your local machine and navigate into the project directory.

```bash
git clone https://github.com/issa-kabore/rag-chatbot-portfolio.git
cd SRAXC
python -m venv venv
```

Activate the virtual environment.

```bash
# On Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### Step 3.2: Install Dependencies

Install all required libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Step 3.3: Configure the API Key

This project uses the **Google Gemini API** for text generation.

1.  Obtain an API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

2.  Create a file named **`.env`** at the root of your project.

3.  Add your API key to this file in the following format:

    ```
    GOOGLE_API_KEY="votre_clé_api_ici"
    ```

### Step 3.4: Create the Vector Database

Modify the `your_portfolio.txt` file with your personal information, then run the `rag_portfolio.py` script to create the FAISS vector index.

```bash
python rag_portfolio.py
```

This will generate the `faiss_portfolio_index` directory, which is essential for the application to function.

-----

## 4\. Local Usage

Once the setup is complete, you can launch the Streamlit application locally.

```bash
streamlit run streamlit_app.py
```

A local server will start, and the application will open automatically in your browser.

-----

## 5\. Deployment

This project is configured for easy and free deployment on **Streamlit Community Cloud** via GitHub.

1.  **Push to GitHub**: Ensure all your files (except `.env` and `venv/`) are committed and pushed to your GitHub repository. The `.gitignore` file should handle this automatically.
2.  **Deploy on Streamlit Cloud**:
      - Log in to [Streamlit Community Cloud](https://streamlit.io/cloud) and click "New app".

      - Select your GitHub repository and the main file (`streamlit_app.py`).

      - In the "Advanced settings," add your `GOOGLE_API_KEY` as a **secret**. Use the format:

        ```
        [secrets]
        GOOGLE_API_KEY="votre_clé_api_ici"
        ```
3.  Click "Deploy\!" and Streamlit will build and launch your app. The application will be accessible via a public URL, perfect for showcasing on your portfolio.



<img width="871" height="853" alt="image" src="https://github.com/user-attachments/assets/9181be1f-5bcb-4aa2-a346-af1f06b8c228" />

