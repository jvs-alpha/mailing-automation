import mysql.connector
import sys

def WriteDB(db,table,firstname,secondname,id,home,fran,gencode,year,month,alpha,number):
    cur = db.cursor()
    cur.execute("INSERT INTO {}(firstname,secondname,id,home,franchise,gender,year,month,alpha,number) VALUE ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(table,firstname,secondname,id,home,fran,gencode,year,month,alpha,number))
    cur.close()
    db.commit()
    return True


if __name__ == "__main__":
    if len(sys.argv) < 14:
        print("Usage: python3 WriteDB.py <user> <passwd> <table> <firstname> <secondname> <id> <home> <fran> <gencode> <year> <month> <alpha> <number>")
    else:
        db = mysql.connector.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database="nric")
        print(WriteDB(db,sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13]))
