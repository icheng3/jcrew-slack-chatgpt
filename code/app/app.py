import os
from slack_bolt import App
from jso import items
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis as RedisVectorStore
from slackbot import SlackBot

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
os.environ['OPENAI_API_KEY'] = "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"
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


bot = SlackBot(app, vectorstore)

@app.message(".*")
def message_handler(message, say, logger):
    bot.handle_message(message, say)

@app.event('app_mention')
def mention_handler(payload, say):
    bot.handle_mention(payload, say)
