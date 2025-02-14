import json

import pika


def publish_email_queue(email, subject, message, scheduleid):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        channel = connection.channel()
        channel.queue_declare(queue="trigger_queue")
        channel.basic_publish(
            exchange="",
            routing_key="trigger_queue",
            body=json.dumps(
                {
                    "email":email,
                    "subject":subject, 
                    "message":message,
                    "scheduleid":scheduleid
                }
            ),
        )

        print(f" [x] Sent {subject} {email}")

        connection.close()
    except Exception as e:
        print(f"Failed to publish message: {e}")
