from flask import Flask,render_template,request
app = Flask(__name__)
import sqlite3

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM user WHERE username=? AND password=?",
                    (request.form["un"],request.form["pwd"]))
        match = len(cur.fetchall())
        if match > 0:
            return "Hello " + request.form["un"]
        else:
            return "user not recognised"
        
@app.route("/signup", methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        f = open("login.txt", "w")
        f.write(request.form['un'])
        f.write("\n")
        f.write(request.form['pwd'])
        f.close()
        return "sign up successful"