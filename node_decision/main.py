import os
import pika

from config import channel


def callback(ch, method, properties, body):
    message_id = properties.message_id
    message_body = body.decode()
    condition = True if message_body.startswith("h") else False
    if condition:
        channel.basic_publish(
            exchange="",
            routing_key=os.getenv("NODE_A_QUEUE_NAME"),
            body=body,
            properties=pika.BasicProperties(message_id=message_id),
        )
    else:
        channel.basic_publish(
            exchange="",
            routing_key=os.getenv("NODE_B_QUEUE_NAME"),
            body=body,
            properties=pika.BasicProperties(message_id=message_id),
        )