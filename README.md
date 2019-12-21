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
* alpha
* number


## TODO
1. Recreate the DB structure with all the elements
2. Create the RegisterNo script
3. The RegisterNo function must return a list containing [register no,alpha,number]
4. Alter the DB APi for the new DB

## TO REMEMBER
* The Value received by the api will be M,F but the values in the DB will be 01,00
