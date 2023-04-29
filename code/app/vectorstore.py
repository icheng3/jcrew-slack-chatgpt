from jcrew_data import items
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis as RedisVectorStore

texts = [
    v['item_name'] for v in items
]

metadatas = [k for k in items]

embedding = OpenAIEmbeddings()

index_name = "products"

redis_url = "redis://localhost:6379"

vectorstore = RedisVectorStore.from_texts(
    texts=texts,
    metadatas=metadatas,
    embedding=embedding,
    index_name=index_name,
    redis_url=redis_url
)
