import mysql.connector
import sys

def ReadDB(db,table):
    cur = db.cursor()
    cur.execute("SELECT * FROM {} ORDER BY No DESC LIMIT 1".format(table))
    data = cur.fetchall()
    cur.close()
    db.commit()
    return data

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 ReadDB.py <user> <passwd> <table>")
    else:
        db = mysql.connector.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database="nric")
        for i in ReadDB(db,sys.argv[3]):
            print(i)
