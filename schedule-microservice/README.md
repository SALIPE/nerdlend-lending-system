# SCHEDULE MICROSERVICE

## Starter Kit

to preview readme file ctrl + shift + v

### to create a venv
python3 -m venv venv

### to activate venv
source venv/bin/activate

### install necessary requirements
cd schedule-microservice
pip install -r requirements.txt

### install Postgres (Linux)
sudo apt update
sudo apt install postgresql postgresql-contrib

### access database configs
sudo -u postgres psql

### create database
CREATE DATABASE schedule_db;

### create a user and grant privileges 
CREATE USER schedule_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE schedule_db TO schedule_user;

### to make migrations
python manage.py makemigrations

### to get out of venv
deactivate