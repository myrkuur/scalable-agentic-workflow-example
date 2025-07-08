from uuid import uuid4
import os
import pika
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from config import channel, collection

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.post("/publish")
def publish_prompt(data: PromptRequest):
    try:
        message_body = data.prompt.encode()
        message_id = str(uuid4())
        channel.basic_publish(
            exchange="",
            routing_key=os.getenv("QUEUE_NAME"),
            body=message_body,
            properties=pika.BasicProperties(message_id=message_id),
        )
        return {
            "status": "success",
            "message": "Prompt published to queue",
            "message_id": message_id,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get/{message_id}")
def get_message(message_id: str):
    try:
        result = collection.find_one({"message_id": message_id})
        result.pop("_id")
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Message not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
