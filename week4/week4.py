from flask import Flask,session
from flask import request
from flask import redirect #導向
import json
import os
from datetime import timedelta



from flask import render_template#樣板

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/")

app.config['SECRET_KEY'] = 'laowangaigebi'

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def Signin():
    Account=request.form["account"]
    Password=request.form["password"]
    if (Account=="test")and(Password=="test"):
        session['username'] = Account
        return redirect('/menber')
    else:
        return redirect('/error')



@app.route("/menber")
def Menber():
    username = session.get('username')
    if username:
        return render_template("indexmenber.html")
    else:
        return redirect('/')

@app.route("/error")
def Error():
    return render_template("indexerror.html")

@app.route("/signout", methods=["GET"])
def Signout():
    session.clear() #清除
#     print("登出")
    return redirect('/')

app.run(port=3000)