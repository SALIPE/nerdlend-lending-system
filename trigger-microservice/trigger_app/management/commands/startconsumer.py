import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from rabbitmq.consumer import Consumer
from django.conf import settings
from django.core.management.base import BaseCommand


def send_confirmation_email(address, subject, body):
    print(f"Sending confirmation email to {address}...")

def send_warning_email(address, subject, body):
    print(f"Sending warning email to {address}...")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

def send_penalty_email(address, subject, body):
    print(f"Sending penalty email to {address}...")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

def trigger_callback(rabbit_message):
    try:
        message = json.loads(rabbit_message)

        action = message.get("action")
        address = message.get("address")
        subject = message.get("subject")
        body = message.get("body")

        if not action or not address or not subject or not body:
            print("Error: Missing required fields in the message.")
            return

        actions = {
            "confirmation": send_confirmation_email,
            "warning": send_warning_email,
            "penalty": send_penalty_email,
        }

        if action in actions:
            actions[action](address, subject, body)
        else:
            print(f"Unknown action: {action}")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON message.")
    except Exception as e:
        print(f"Error processing message: {e}")

# class Command(BaseCommand):
#     help = 'Starts RabbitMQ Consumer'

#     def handle(self, *args, **kwargs):
#         consumer = Consumer(queue="trigger_queue", callback=trigger_callback)
#         consumer.start()

