import os

from config import channel
from main import callback


def main():
    channel.basic_consume(queue=os.getenv("NODE_B_QUEUE_NAME"), on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    main()
