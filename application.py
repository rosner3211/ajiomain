from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://www.clkmg.com/nitinteotia3/zippyloan/{keyword}/{device}/{campaignid}", code=302)
