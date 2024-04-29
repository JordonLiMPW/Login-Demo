from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        f = open("login.txt", "r")
        un = f.read()
        pwd = f.read()
        f.close()
        print(un)
        print(len(un))
        if un[:-1] == request.form and pwd == request.form["pw"]:
            return "Hello " + un
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