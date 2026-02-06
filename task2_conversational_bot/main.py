import os
from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Load OpenAI key from .env
load_dotenv()

# ---------------- CONFIG ----------------
# Your resume file (spaces are OK)
PDF_FILENAME = "Task2_Conversational_Resume_Bot.pdf"
# --------------------------------------

def main():
    if not os.path.exists(PDF_FILENAME):
        print(f"❌ Resume PDF not found: {PDF_FILENAME}")
        print("Make sure the PDF is in the same folder as main.py")
        return

    print("📄 Loading resume PDF...")
    loader = PyPDFLoader(PDF_FILENAME)
    documents = loader.load()

    print("🧠 Creating embeddings and vector store...")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    llm = ChatOpenAI(temperature=0)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    print("\n✅ Resume Chatbot Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        result = qa({"question": user_input})
        answer = result.get("answer", "")

        print("\nBot:", answer)
        print("-" * 60)


if __name__ == "__main__":
    main()
