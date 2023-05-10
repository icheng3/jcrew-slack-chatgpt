# import os
# import pinecone

# pinecone.init(api_key=os.environ["PINECONE_API"], environment=os.environ["PINECONE_ENV"])

# from langchain.schema import Document
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import Pinecone
# from jcrew_data import items

# embeddings = OpenAIEmbeddings()
# # create new index
# pinecone.create_index("langchain-self-retriever-demo", dimension=1536)

# texts = [
#     v['item_name'] for v in items
# ]

# metadatas = [k for k in items]

# embedding = OpenAIEmbeddings()

# index_name = "langchain-self-retriever-demo"

# vectorstore = Pinecone.from_texts(
#     texts=texts,
#     metadatas=metadatas,
#     embedding=embedding,
#     index_name=index_name
# )

# from langchain.llms import OpenAI
# from langchain.retrievers import 
# retrievers.self_query.base import SelfQueryRetriever
# from langchain.chains.query_constructor.base import AttributeInfo

# metadata_field_info=[
#     AttributeInfo(
#         name="genre",
#         description="The genre of the movie", 
#         type="string or list[string]", 
#     ),
#     AttributeInfo(
#         name="year",
#         description="The year the movie was released", 
#         type="integer", 
#     ),
#     AttributeInfo(
#         name="director",
#         description="The name of the movie director", 
#         type="string", 
#     ),
#     AttributeInfo(
#         name="rating",
#         description="A 1-10 rating for the movie",
#         type="float"
#     ),
# ]
# document_content_description = "Brief summary of a movie"
# llm = OpenAI(temperature=0)
# retriever = SelfQueryRetriever.from_llm(llm, vectorstore, document_content_description, metadata_field_info, verbose=True)
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import FAISS
# from langchain.document_loaders import TextLoader

# os.environ['OPENAI_API_KEY'] = 'OPENAI_API_KEY'

