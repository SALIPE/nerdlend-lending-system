#!/bin/sh

STAGE=$1
REGISTRY=registry.coding.ipb.pt
IMAGE_NAME=$REGISTRY/sdt-project-group-07

AUTH_IMAGE_VERSION=$IMAGE_NAME/auth:$STAGE
PRODUCT_IMAGE_VERSION=$IMAGE_NAME/product:$STAGE
CUSTOMER_IMAGE_VERSION=$IMAGE_NAME/customer:$STAGE
SCHEDULE_IMAGE_VERSION=$IMAGE_NAME/schedule:$STAGE
TRIGGER_IMAGE_VERSION=$IMAGE_NAME/trigger:$STAGE
GATEWAY_IMAGE_VERSION=$IMAGE_NAME/gateway:$STAGE
QUEUE_IMAGE_VERSION=$IMAGE_NAME/queue:$STAGE
FRONT_IMAGE_VERSION=$IMAGE_NAME/frontend:$STAGE


echo "Setting up Docker Buildx..."
docker buildx create --use

echo "Building and pushing Docker image with Buildx... "
echo "$2" | docker login $REGISTRY -u student --password-stdin

docker buildx build --platform linux/amd64 -t $GATEWAY_IMAGE_VERSION -t $GATEWAY_IMAGE_VERSION --push ./gateway

docker buildx build --platform linux/amd64 -t $AUTH_IMAGE_VERSION -t $AUTH_IMAGE_VERSION --push ./auth-microservice

docker buildx build --platform linux/amd64 -t $PRODUCT_IMAGE_VERSION -t $PRODUCT_IMAGE_VERSION --push ./product-microservice

docker buildx build --platform linux/amd64 -t $CUSTOMER_IMAGE_VERSION -t $CUSTOMER_IMAGE_VERSION --push ./customer-microservice

docker buildx build --platform linux/amd64 -t $SCHEDULE_IMAGE_VERSION -t $SCHEDULE_IMAGE_VERSION --push ./schedule-microservice

docker buildx build --platform linux/amd64 -t $TRIGGER_IMAGE_VERSION -t $TRIGGER_IMAGE_VERSION --push ./trigger-microservice

docker buildx build --platform linux/amd64 -t $QUEUE_IMAGE_VERSION -t $QUEUE_IMAGE_VERSION --push ./queue

docker buildx build --platform linux/amd64 -t $FRONT_IMAGE_VERSION -t $FRONT_IMAGE_VERSION --push ./frontend
