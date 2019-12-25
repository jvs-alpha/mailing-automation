import mysql.connector

def ReadDB(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM Users ORDER BY No DESC LIMIT 1")
    data = cur.fetchall()
    cur.close()
    return data

if __name__ == "__main__":
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="jesuslovesyou",
    database="nric")
    for i in ReadDB(db):
        print(i)
