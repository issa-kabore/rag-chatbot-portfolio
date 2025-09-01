import streamlit as st
from src.rag_chain import setup_rag_chain

# --- 1. RAG Chain Setup ---
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = setup_rag_chain()
if "messages" not in st.session_state:
    st.session_state.messages = []


# --- 2. Chat Logic ---
def handle_chat_input(prompt):
    """Handles both user input and pre-recorded questions."""
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from the RAG chain
    with st.spinner("Réponse en cours..."):
        response = ""
        if st.session_state.rag_chain:
            try:
                result = st.session_state.rag_chain.invoke({"query": prompt})
                response = result["result"]
            except Exception as e:
                response = f"Une erreur s'est produite : {str(e)}"
        else:
            response = "Le système RAG n'est pas correctement initialisé."

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


# --- 3. Streamlit Interface ---

st.title("SRAXC (Self-Reflective AI eXpert Chatbot)")
st.subheader("Posez des questions sur mon portfolio, mes compétences et mes projets.")
st.write("La réponse est générée à partir d'un document personnel.")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Display pre-recorded questions as buttons
st.markdown("### Ou essayez ces questions :")
# col1, col2, col3 = st.columns(3)

# with col1:
#     if st.button("Qui est Issa Kabore ?"):
#         handle_chat_input("Qui est Issa Kabore ?")

# with col2:
#     if st.button("Quelles sont ses compétences techniques ?"):
#         handle_chat_input("Quelles sont ses compétences techniques ?")

# with col3:
#     if st.button("Parle-moi de ses projets. "):
#         handle_chat_input("Parle-moi de ses projets. ")

if st.button("Qui est Issa Kabore ?"):
    handle_chat_input("Qui est Issa Kabore ?")

if st.button("Quelles sont ses compétences techniques ?"):
    handle_chat_input("Quelles sont ses compétences techniques ?")

if st.button("Parle-moi de ses projets."):
    handle_chat_input("Parle-moi de ses projets.")
    
# Handle user input from the chat box
if prompt := st.chat_input("Votre question..."):
    handle_chat_input(prompt)
