import json
from datetime import datetime, timedelta

import jwt
import requests
from django.conf import settings

from rabbitmq.messages import publish_email_queue

JWT_SECRET = settings.SECRET_KEY
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_DELTA = timedelta(hours=1)

def generate_internal_jwt_token():
    payload = {
        'internal_user': "robo",
        'exp': datetime.utcnow() + JWT_EXPIRATION_DELTA,  
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token



def make_internal_request(url, data=None):
    """
    Make an HTTP request with a bearer token.

    Args:
        url (str): The endpoint URL.
        token (str): The bearer token for authentication.
        data (dict, optional): Data to be sent with the request (e.g., for POST requests).

    Returns:
        Response: The response object from the HTTP request.
    """
    token = generate_internal_jwt_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',  # Adjust the content type as needed
    }

    try:
        # Example: Making a GET request
        if data is None:
            response = requests.get(f'http://{url}', headers=headers)
        else:
            # Example: Making a POST request with data
            response = requests.post(f'http://{url}', headers=headers, json=data)
        
        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
        
        # Return the response object
        return json.loads(response.text)

    except requests.exceptions.RequestException as e:
        # Handle exceptions (e.g., network error, invalid response, etc.)
        print(f"An error occurred: {e}")
        return None


def send_create_notification(schedule, customer,scheduleid):

        # to future: we have to recover user info to assemble email using schedule.cv_customer_id
        # email address
        # user name

        message = f"""
                Dear Customer {customer.get("ccname")},

                We are pleased to confirm the details of your new schedule:

                - Due Date: {schedule.get("cdduedate")}
                - Withdraw Date: {schedule.get("cdwithdrawdate")}
                - Value: {schedule.get("cvvalue")}

                Please ensure that the due date is met to avoid any penalties or disruptions. Should you have any questions or need further assistance, feel free to contact us.

                Thank you for choosing our service!

                Best regards,
                Nerdlend
            """
        try:
            publish_email_queue(customer.get("ccemail"),"Confirmation email for renting", message,scheduleid)
        except Exception as e:
            # Log or handle the exception
            print(f"Failed to send message to RabbitMQ: {e}")

def send_returned_notification(schedule, customer,scheduleid, productlist):

        # to future: we have to recover user info to assemble email using schedule.cv_customer_id
        # email address
        # user name

        message = f"""
                Dear Customer {customer.get("ccname")},

                Lend returned:

                - Schedule: {schedule}
                - Products: {productlist}

                Thank you for choosing our service!

                Best regards,
                Nerdlend
            """
        try:
            publish_email_queue(customer.get("ccemail"),"Confirmation email for renting return", message,scheduleid)
        except Exception as e:
            # Log or handle the exception
            print(f"Failed to send message to RabbitMQ: {e}")
