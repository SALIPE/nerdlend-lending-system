FROM python:3.10
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . /app

# Run the application
CMD ["python", "queue_consumer.py"]