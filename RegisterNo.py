import datetime
import mysql.connector

def RegisterNo(db,firstname,lastname,home,fran,gen):
    year = datetime.datetime.utcnow().year
    month = datetime.datetime.utcnow().month
    if gen == "M":
        gencode = "01"
    else:
        gencode = "00"
    cur = db.corsor()
    data = cur.execute("SELECT * FROM Users")
    cur.close()
    if data[-1][-1] == month or date[-1][-2] == year:
        alpha = "A"
    else:
        number = "001"


if __name__ == "__main__":
