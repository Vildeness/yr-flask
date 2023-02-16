from flask import Flask, render_template
import requests
from yr import hent_temp

app = Flask(__name__)



@app.route("/")
def index():
    tempratur = hent_temp(59.81, 10.52)
    print(f"Tempratur: {tempratur}")
    sted = "Sandvika"
    return  render_template("index.html", sted=sted, tempratur=tempratur)

@app.route("/trondheim")
def trondheim():
    tempratur = hent_temp()
    print(f"Tempratur: {tempratur}")
    sted = "Trondheim"
    return render_template("index.html", sted=sted, tempratur=tempratur)

@app.route("/")
def kristiansand():
    tempratur = hent_temp()
    print(f"Tempratur: {tempratur}")
    sted = "kristiasand"
    return render_template("index.html", sted=sted, tempratur=tempratur)

@app.route("/")
def bergen():
    tempratur = hent_temp()
    print(f"Tempratur: {tempratur}")
    sted = "Bergen"
    return render_template("index.html", sted=sted, tempratur=tempratur)

@app.route("/")
def tromsø():
    tempratur = hent_temp()
    print(f"Tempratur: {tempratur}")
    sted = "tromsø"
    return render_template("index.html", sted=sted, tempratur=tempratur)

@app.route("/")
def stavanger():
    tempratur = hent_temp()
    print(f"Tempratur: {tempratur}")
    sted = "stavanger"
    return render_template("index.html", sted=sted, tempratur=tempratur)

