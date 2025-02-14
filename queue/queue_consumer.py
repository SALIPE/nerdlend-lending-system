import json
import os

import pika
import requests
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("RABBIT_MQ_HOST", default="rabbitmq")
port = os.getenv("RABBIT_MQ_PORT", default="5672")
params = pika.URLParameters(f"amqp://{host}:{port}")

EMAIL_SERVICE_URL = "http://trigger-services:8005"


connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="trigger_queue")
# channel.basic_qos(prefetch_count=1) # Prevent one consumer from being overwhelmed

def callback(ch, method, properties, body):
    try:
        payload = json.loads(body)

        # Validate payload
        required_fields = ["email", "subject", "message"]
        if not all(field in payload for field in required_fields):
            print(f" [!] Invalid payload: {payload}")
            return None

        # Forward to Notification Service
        response = requests.post(EMAIL_SERVICE_URL + "/send-email", json=payload)
        response.raise_for_status()
        print(f" Email sended: {payload}")
    except Exception as e:
        print(f" [!] Error processing message: {str(e)}")



channel.basic_consume(
    queue="trigger_queue", on_message_callback=callback, auto_ack=True
)

print(" [*] Waiting for messages. To exit press CTRL+C")

channel.start_consuming()

channel.close()
