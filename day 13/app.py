from flask import Flask, render_template
app=Flask(__name__)

@app.get('/')
@app.get('/home')
def home():
    return render_template('index.html', name="BOBTHEDOG")

@app.get('/about')
def about():
    return render_template('about.html')

@app.get('/login')
def login():
    return render_template('login.html')

@app.get('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True)
