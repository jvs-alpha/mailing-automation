from flask import Flask,request
from flask_mysqldb import MySQL
import mysql.connector
from RegisterNo import *
import datetime

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MUSQL_USER"] = "root"
app.config["MUSQL_PASSWORD"] = "jesuslovesyou"
app.config["MYSQL_DB"] = "nric"
mysql = MySQL(app)
year = datetime.datetime.utcnow().year
month = datetime.datetime.utcnow().month
db = mysql.connector.connect(
host="localhost",
user="root",
passwd="jesuslovesyou",
database="nric")
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = request.get_json()
        firstname = data["fname"]
        secondname = data["sname"]
        home = data["home"]
        fran = data["fran"]
        gen = data["gen"]
        rdata = RegisterNo(db,home,fran,gen)
        id = rdata[0]
        gencode = rdata[1]
        alpha = rdata[2]
        number = rdata[3]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Users(firstname,secondname,id,home,franchise,gender,year,month,alpha,number) VALUE ('{}','{}','{}','{}','{}','{}'.'{}','{}','{}','{}')".format(firstname,lastname,id,home,fran,gencode,year,month,alpha,number))
        pdat = cur.execute("SELECT * FROM Users")
        print(pdat)
        mysql.connection.commit()
        cur.close()
        return "success"
    else:
        return "NRIC SERVER"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="3000",debug=True)
