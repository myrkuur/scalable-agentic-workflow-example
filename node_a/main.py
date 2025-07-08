from config import collection

def callback(ch, method, properties, body):
    message_id = properties.message_id
    message_body = body.decode()
    collection.insert_one({"message_id": message_id, "message_body": message_body, "node": "a"})
    print(" [x] Received %r" % body)
