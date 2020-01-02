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
* add the superuser and fran admin users
* Check the RegisterNo is working all the ways
* Modify the MailService to send pdf
* Modify the Certificate.py to accept two names insted of one and the RegNo
* make the DB API more secure
* Insert the data to the server
* Learn about neo4js

## WORKING ON
* changing the system from uni-user to multi-user
* ReadDB is in progress

## TO REMEMBER
* The Value received by the api will be M,F but the values in the DB will be 01,00

## Modules Function
* ReadDB.py - Reading the data from the DB
