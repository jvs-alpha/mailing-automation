import datetime
import mysql.connector
import sys

def RegisterNo(db,firstname,lastname,home,fran,gen):
    year = datetime.datetime.utcnow().year
    month = datetime.datetime.utcnow().month
    if gen == "M":
        gencode = "01"
    else:
        gencode = "00"
    cur = db.cursor()
    data = cur.execute("SELECT * FROM Users")
    cur.close()
    if data[-1][-3] == month or date[-1][-4] == year:
        alpha = "A"
        number = "001"
    elif data[-1][-2] == "Z" and int(data[-1][-1]) == 9999 and data[-1][-3] == month:
        return("Reached the limit")
    elif int(data[-1][-1]) == 9999:
        ordnum = ord(data[-1][-2])
        ordnum += 1
        alpha = chr(ordnumber)
        number = "0001"
    else:
        alpha = data[-1][-2]
        number = int(data[-1][-1])
        number += 1
    registerno = "".join(home,fran,str(year),str(month),gencode,str(alpha),str(number))
    redata = [registerno,alpha,number]


if __name__ == "__main__":
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="jesuslovesyou",
    database="nric")
    print(RegisterNo(db,sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))
