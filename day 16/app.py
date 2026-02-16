from flask import Flask, render_template, request,url_for,redirect,session

app=Flask(__name__)

app.secret_key="suhdviusvbhdsivugbsdi"

bekar = ""

@app.route('/', methods=["GET","POST"])
def home():

    data_incoming=""

    if request.method == "POST":
        data_incoming = request.form.get("input_data")
        data_incoming_p=request.form.get("input_password")
        print(data_incoming)
        if data_incoming == "admin" and data_incoming_p == "password":
            session["user"] = data_incoming
            return redirect(url_for("dashboards"))
        
        
    return render_template("index.html",data_incoming=data_incoming)

@app.route("/dashboard")
def dashboards():
    return render_template("dashboard.html")
app.run(debug=True)