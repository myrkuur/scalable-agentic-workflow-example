import os
from pymongo import MongoClient
import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=os.getenv("RABBITMQ_HOST"),
        port=int(os.getenv("RABBITMQ_PORT")),
        credentials=pika.PlainCredentials(
            os.getenv("RABBITMQ_USER"), os.getenv("RABBITMQ_PASSWORD")
        ),
    )
)
channel = connection.channel()
channel.queue_declare(queue=os.getenv("NODE_B_QUEUE_NAME"))


client = MongoClient(os.getenv("MONGO_HOST"), int(os.getenv("MONGO_PORT")))
db = client[os.getenv("MONGO_DATABASE")]
collection = db[os.getenv("MONGO_COLLECTION")]
