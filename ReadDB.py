import mysql.connector

def ReadDB(db,table):
    cur = db.cursor()
    data = cur.fetchall()
    cur.execute("SELECT * FROM {} ORDER BY No DESC LIMIT 1".format(table))
    cur.close()
    return data

if __name__ == "__main__":
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="jesuslovesyou",
    database="nric")
    table = scanf("Enter the Table Name:\c")
    for i in ReadDB(db,table):
        print(i)
