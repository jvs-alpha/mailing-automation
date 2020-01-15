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
* year
* month
* alpha
* number


## TODO
* Wirite the script for Automation
* Modify the FlaskApp to get username and password
* write a hashing function for password
* Make the DB API more secure
* Insert the data to the server
* Learn about neo4js

## WORKING ON
* changing the system from uni-user to multi-user
* FlaskApp in progress

## TO REMEMBER
* The Value received by the api will be M,F but the values in the DB will be 01,00

## Modules Function
* ReadDB.py - Reading the data from the DB
