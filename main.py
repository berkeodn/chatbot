import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Template for conversation
template = """
Answer the question below.

Here is the conversation history: {context}  

Question: {question}

Answer: 
"""

# Initialize the Ollama LLM
model = OllamaLLM(model="llama3")

# Create prompt from template
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit UI
st.title("Büşra's Personal AI Assistant")

# Initialize conversation history in Streamlit session state
if 'context' not in st.session_state:
    st.session_state.context = ""

# Introduction text
st.write("Büşra'nın kişisel yapay zeka asistanına hoş geldiniz. Size nasıl yardımcı olabilirim? "
         "Türkçem biraz kötü, ama elimden gelenin en iyisini yapacağım. Daha iyi sonuç almak için lütfen İngilizce kullanın.")

# User input via Streamlit text input box
user_input = st.text_input("Siz: ", "")

# When user enters a question
if user_input:
    # Get AI response
    result = chain.invoke({"context": st.session_state.context, "question": user_input})
    
    # Display the AI response
    st.write(f"AI: {result}")
    
    # Update the conversation context with the user input and AI response
    st.session_state.context += f"\nSiz: {user_input}\nAI: {result}"

# Option to reset the conversation
if st.button('Sohbeti Sıfırla'):
    st.session_state.context = ""
    st.write("Sohbet sıfırlandı.")
