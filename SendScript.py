from WriteDB import *
from Certificate import *
from MailService import *
from RegisterNo import *
import mysql.connector
import datetime
import os
import sys
import csv

year = datetime.datetime.utcnow().year
month = datetime.datetime.utcnow().month

def SendScript(csv_raw,user,passwd,table,home,fran):
    f = open(csv_raw,newline="")
    csvdata = csv.reader(f,delimiter=",",quotechar="|")
    db = mysql.connector.connect(
    host="localhost",
    user=user,
    passwd=passwd,
    database="nric")
    check = 0
    for data in csvdata:
        if check == 0:
            check = 1
            continue
        firstname = data[0]
        secondname = data[1]
        rdata = RegisterNo(user,passwd,table,home,fran,data[4])
        if rdata == "Reached the limit":
            f.close()
            db.close()
            print("Reached the limit")
            sys.exit(0)
        id = rdata[0]
        gencode = rdata[1]
        alpha = rdata[2]
        number = rdata[3]
        check = WriteDB(db,table,firstname,secondname,id,home,fran,gencode,year,month,alpha,number)
        print("Writen Name: {} ID: {}".format(firstname,id))
        Certificate("{} {}".foramt(firstname,secondname),id)
    f.close()
    db.close()
if __name__ == "__main__":
    SendScript(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
