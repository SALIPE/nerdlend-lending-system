# NERDLEND - LENDING SYSTEM

NerdLend is a software system developed for managing rental stores. This project was designed with a microservices architecture in mind, leveraging Django for backend services, React.js for the frontend, and several other technologies to ensure scalability, security, and efficiency.

## 🚀 Features

- **Microservices Architecture**: Each core functionality is developed as an independent Django microservice.
- **JWT Authentication**: Secure authentication and authorization using JSON Web Tokens (JWT).
- **Nginx as Gateway**: Acts as a reverse proxy to route requests efficiently.
- **React.js Frontend**: A modern, dynamic, and responsive UI built with React.js.
- **RabbitMQ for Queue Processing**: Asynchronous task handling using RabbitMQ.
- **Scalable and Modular Design**: Ensuring flexibility for future enhancements.

## 🛠️ Technologies Used

- **Backend**: Django (for microservices)
- **Frontend**: React.js
- **API Gateway**: Nginx
- **Authentication**: JWT
- **Message Queue**: RabbitMQ
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose

## 📦 Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Docker & Docker Compose
- Python (for running Django microservices)
- Node.js (for running the React frontend)

### Steps

1. **Clone the repository**:

   ```sh
   git clone https://github.com/SALIPE/nerdlend-lending-system
   cd nerdlend-lending-system
   ```

2. **Set up environment variables**:

   - Create the `.env` and configure it accordingly with the necessary variables for your use.

3. **Start Services with Docker**:

   ```sh
   docker-compose up --build
   ```

4. **To Run Docker Locally**:

    ```sh
    python3 docker-compose-local-run.py
    ```

5. **To see what is happening on port**
    ```sh
    sudo lsof -i :5432
    ```

## 📝 Observation
This project was originally hosted on GitLab and has been migrated to GitHub for better collaboration and accessibility.




