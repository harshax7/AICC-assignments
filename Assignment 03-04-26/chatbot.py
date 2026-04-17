

from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

llm = Ollama(model="llama3")
loader = TextLoader("data.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings()

db = FAISS.from_documents(docs, embeddings)
retriever = db.as_retriever()

print("🤖 Chatbot (with DATA) is ready! Type 'exit' to stop.\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    retrieved_docs = retriever.get_relevant_documents(query)
    context = " ".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
    Answer ONLY from the given context.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    print("Bot:", response)