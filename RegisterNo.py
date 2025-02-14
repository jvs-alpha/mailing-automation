import datetime
import mysql.connector
import sys
from ReadDB import ReadDB


def RegisterNo(user,passwd,table,home,fran,gen):
    # For every read we need to refresh the database so we need to connect to it every time
    db = mysql.connector.connect(
    host="localhost",
    user=user,
    passwd=passwd,
    database="nric")
    year = datetime.datetime.utcnow().year
    month = datetime.datetime.utcnow().month
    # This is for finding the month length
    if month < 10:
        month = "0{}".format(month)
    else:
        month = str(month)
    # Convertion of M,F to 01,00
    if gen == "Male":
        gencode = "01"
    else:
        gencode = "00"
    # This is for reading the alst entry of the database
    data = ReadDB(db,table)
    # data[-1][-3] = last entered month
    # data[1][-4] = last enteres year
    # data[1][-2] = last enteres alpha
    # data[1][-1] = last enteres number
    if int(data[-1][-3]) != int(month) or int(data[-1][-4]) != year:
        alpha = "A"
        number = "0001"
    elif data[-1][-2] == "Z" and int(data[-1][-1]) == 9999 and int(data[-1][-3]) == int(month):
        return("Reached the limit")
    elif int(data[-1][-1]) == 9999:
        ordnum = ord(data[-1][-2])
        ordnum += 1
        alpha = chr(ordnum)
        number = "0001"
    else:
        alpha = data[-1][-2]
        number = int(data[-1][-1])
        number += 1
        if number >= 1 and number < 10:
            number = "000{}".format(number)
        elif number >= 10 and number < 100:
            number = "00{}".format(number)
        elif number >= 100 and number < 1000:
            number = "0{}".format(number)
        else:
            number = str(number)
    registerno = "{}{}{}{}{}{}{}".format(home,fran,year,month,gencode,alpha,number)
    redata = [registerno,gencode,alpha,number]
    return redata


if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("Usage: python3 RegisterNo.py <user> <passwd> <table> <home> <fran> <gen>")
    else:
        print(RegisterNo(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]))
