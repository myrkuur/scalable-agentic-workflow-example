import os
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
channel.queue_declare(queue=os.getenv("QUEUE_NAME"))