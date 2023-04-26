import os
from jcrew_prod_retriever import RedisProductRetriever
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis as RedisVectorStore
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import (
    ConversationalRetrievalChain,
    LLMChain)
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate
from api_keys import open_ai_key

# set your openAI api key as an environment variable
os.environ['OPENAI_API_KEY'] = open_ai_key
 
# data that will be embedded and converted to vectors
texts = [
    v['item_name'] for v in product_json
]
 
# product metadata that we'll store along our vectors
metadatas = list(k.values() for k in product_json)
 
# we will use OpenAI as our embeddings provider
embedding = OpenAIEmbeddings()
 
# name of the Redis search index to create
index_name = "products"
 
# assumes you have a redis stack server running on local host
redis_url = "redis://localhost:6379"

# create and load redis with documents
vectorstore = RedisVectorStore.from_texts(
    texts=texts,
    metadatas=metadatas,
    embedding=embedding,
    index_name=index_name,
    redis_url=redis_url
)

template = """Given the following chat history and a follow up question, rephrase the follow up input question to be a standalone question.
Or end the conversation if it seems like it's done.
Chat History:\"""
{chat_history}
\"""
Follow Up Input: \"""
{question}
\"""
Standalone question:"""
 
condense_question_prompt = PromptTemplate.from_template(template)
 
template = """You are a friendly, conversational retail shopping assistant. Use the following context including product names, descriptions, and keywords to show the shopper whats available, help find what they want, and answer any questions.
 
It's ok if you don't know the answer.
Context:\"""
 
{context}
\"""
Question:\"
\"""
 
Helpful Answer:"""
 
qa_prompt= PromptTemplate.from_template(template)

# define two LLM models from OpenAI
llm = OpenAI(temperature=0)
 
streaming_llm = OpenAI(
    streaming=True,
    callback_manager=CallbackManager([
        StreamingStdOutCallbackHandler()
    ]),
    verbose=True,
    max_tokens=150,
    temperature=0.2
)
 
# use the LLM Chain to create a question creation chain
question_generator = LLMChain(
    llm=llm,
    prompt=condense_question_prompt
)
 
# use the streaming LLM to create a question answering chain
doc_chain = load_qa_chain(
    llm=streaming_llm,
    chain_type="stuff",
    prompt=qa_prompt
)

redis_product_retriever = RedisProductRetriever(vectorstore=vectorstore)
 
chatbot = ConversationalRetrievalChain(
    retriever=redis_product_retriever,
    combine_docs_chain=doc_chain,
    question_generator=question_generator
)

# create a chat history buffer
chat_history = []
# gather user input for the first question to kick off the bot
question = input("Hi! What are you looking for today?")
 
# keep the bot running in a loop to simulate a conversation
while True:
    result = chatbot(
        {"question": question, "chat_history": chat_history}
    )
    print("\n")
    chat_history.append((result["question"], result["answer"]))
    question = input()