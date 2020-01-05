import mysql.connector
import getpass

def ReadDB(db,table):
    cur = db.cursor()
    cur.execute("SELECT * FROM {} ORDER BY No DESC LIMIT 1".format(table))
    data = cur.fetchall()
    cur.close()
    return data

if __name__ == "__main__":
    user = input("Enter the User Name: ")
    passwd = getpass.getpass()
    table = input("Enter the Table Name: ")
    db = mysql.connector.connect(
    host="localhost",
    user=user,
    passwd=passwd,
    database="nric")
    for i in ReadDB(db,table):
        print(i)
