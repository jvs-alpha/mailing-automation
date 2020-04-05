import mysql.connector
import sys
import argparse

def ReadDB(db,table):
    cur = db.cursor()
    cur.execute("SELECT * FROM {} ORDER BY No DESC LIMIT 1".format(table))
    data = cur.fetchall()
    cur.close()
    db.commit()
    return data

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="This is a Database Read Script")
    parse.add_argument("User",type=str,help="This is the Database Username")
    parse.add_argument("Password",type=str,help="This is the Database Password")
    parse.add_argument("Table",type=str,help="This is the Database Table")
    argv = parse.parse_args()

    db = mysql.connector.connect(
        host="localhost",
        user=argv.User,
        passwd=argv.Password,
        database="nric"
        
    )
    for i in ReadDB(db,argv.Table):
        print(i)
