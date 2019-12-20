# Automation of mailing service

## Needed functions
* Get the information about the receiver from a web interface
* Send the information to a backend service
* Send the email with the template to the receiver
* Secure the backend service with SSL Certificate

## Modules used
* smtplib - python3
* flask - python3
* flask_musqldb - python3
* mysql-cohnnector - python3
* base64 - python3
* json - python3

## Database parameters
* firstname
* lastname
* id
* home division
* franchise
* gender


## Procedure for creating the DB
* create the database structure using mysql
* create the api for the DB
