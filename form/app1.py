from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/help",methods = ["POST"])
def help():
    name = request.form.get("name")
    return "hello"+name

app.run(debug=True)