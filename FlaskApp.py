from flask import Flask,request
from RegisterNo import *
import datetime

app = Flask(__name__)
year = datetime.datetime.utcnow().year
month = datetime.datetime.utcnow().month
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = request.get_json()
        firstname = data["fname"]
        secondname = data["sname"]
        home = data["home"]
        fran = data["fran"]
        gen = data["gen"]
        rdata = RegisterNo(home,fran,gen)
        id = rdata[0]
        gencode = rdata[1]
        alpha = rdata[2]
        number = rdata[3]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Users(firstname,secondname,id,home,franchise,gender,year,month,alpha,number) VALUE ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(firstname,secondname,id,home,fran,gencode,year,month,alpha,number))
        mysql.connection.commit()
        cur.close()
        return "success"
    else:
        return "NRIC SERVER"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="3000",debug=True)
