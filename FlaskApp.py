from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///register.db"
db = SQLAlchemy(app)

class students(db.Model):
    name = db.Column(db.String(2),nullable=False)
    number = db.Column(db.String(10),nullable=False)
    home = db.Column(db.String(3),nullable=False)
    frachise = db.Column(db.string(4),nullable=False)
    # replace the year with the datetime module
    year = db.Column(db.String(4),nullable=False)
    month = db.Column(db.String(2),nullable=False)
    # gender
    alpha = db.Column(db.String(1),nullable=False)
    number = db.Column(db.Integer,nullable=False)
    id = db.Column(db.String(18),primary_key=True,nullable=False)


    def __rep__(self):
        return "<User %r>" % self.username

@app.route("/",methods=["GET"])
def message():
    return "nric"

@app.route("/users")
def
