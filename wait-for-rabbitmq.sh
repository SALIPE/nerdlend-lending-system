#!/bin/bash

RABBITMQ_HOST=${RABBITMQ_HOST:-rabbitmq}
RABBITMQ_PORT=${RABBITMQ_PORT:-5672}

echo "Waiting for RabbitMQ at ${RABBITMQ_HOST}:${RABBITMQ_PORT}..."

while ! nc -z $RABBITMQ_HOST $RABBITMQ_PORT; do
  echo "RabbitMQ is not available yet. Retrying in 2 seconds..."
  sleep 2
done

echo "RabbitMQ is up and running. Starting the consumer..."
exec "$@"
