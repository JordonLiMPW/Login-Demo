from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    user = request.args.get('un')
    password = request.args.get('pwd')
    if user == None:
        return render_template("index.html")
    elif user == 'bob' and password == "114514":
        return "Hello " + user
    else:
        return "user not recognised"