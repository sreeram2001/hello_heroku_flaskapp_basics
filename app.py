from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key  = "abcdefghijklm"

@app.route("/home")


#function to render html template
def index():
    return render_template("index.html")


#new route to interact with server
#CONNECT a function to the route

@app.route("/hello", methods=["POST","GET"])

def hello():
    p = str(request.form['inputname'])
    flash("Hello " + p + " Nice to have you here")
    return render_template("index.html")
    
