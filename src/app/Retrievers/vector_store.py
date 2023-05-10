from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
import os
from jcrew_data import items
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
print(len(items))
embeddings = OpenAIEmbeddings()
# create new index

texts = [
    v['item_name'] for v in items
]

metadatas = [k for k in items]

embedding = OpenAIEmbeddings()


vectorstore = FAISS.from_texts(
    texts=texts,
    metadatas=metadatas,
    embedding=embedding
)
