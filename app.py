from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        user = request.form['un']
        password = request.form['pwd']
        if user == 'bob' and password == "114514":
            return "Hello " + user
        else:
            return "user not recognised"
        
@app.route("/signup")
def signup():
    return render_template("signup.html")