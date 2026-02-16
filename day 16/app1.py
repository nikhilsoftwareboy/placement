from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/blog/<int:id>')
@app.route('/<id>')
def home(id):
    return render_template("dym.html",id=id)

@app.route('/price/<float:paisa>')
def price(paisa):
    return render_template("pa.html",paisa=paisa)

@app.route('/pat/<path:file>')
def path(file):
    return render_template("path.html", file=file)

app.run(debug="True") 