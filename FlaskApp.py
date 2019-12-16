from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///register.db"
db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column(db.String(20),primary_key=True,unique=True,nullable=False)
    name = db.Column(db.String(200),unique=True,nullable=False)
    cls = db.Column(db.String(50),nullable=False)


    def __rep__(self):
        return "<User %r>" % self.username

@app.route("/",methods=["GET"])
def message():
    return "jvs testing"

@app.route("/users")
def 
