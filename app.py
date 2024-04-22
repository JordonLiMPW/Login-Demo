from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    user = request.args.get('user')
    password = request.args.get('password')
    if user == None:
        return render_template("index.html")
    elif user == 'bob':
        return "Hello " + user
    else:
        return "user not recognised"