from flask import Flask,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MUSQL_USER"] = "root"
app.config["MUSQL_PASSWORD"] = "jesuslovesyou"
app.config["MYSQL_DB"] = "nric"
mysql = MySQL(app)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = request.get_json()
        firstname = data["fname"]
        lastname = data["lname"]
        cur = mysql.connectio.cursor()
        cur.execute("INSERT INTO Users(firstname,lastname) VALUE ('{}','{}')".format(firstname,lastname))
        pdat = cur.execute("SELECT * FROM Users")
        print(pdat)
        mysql.connection.commit()
        cur.close()
        return "success"
    else:
        return "NRIC SERVER"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="3000",debug=True)
