from flask import Flask, render_template, redirect, jsonify
import pymongo
import pandas as pd
import get_data

app = Flask(__name__)

#Get the Data for NBA
conn = 'mongodb+srv://sabu:cp3@cluster0.suglk.mongodb.net/test'
client = pymongo.MongoClient(conn)
# Declare the database
db = client.NBA_NCAA

@app.route("/")
def index():
    #Home page
    return render_template("index.html")

@app.route("/data")
def data():
    #Data comparison page
    return render_template("datapage.html")

@app.route("/data/<player>")
def dataplayer(player):
    #Go to a specific player's comparison page used in tooltip
    return render_template("dataplayerpage.html", playername = player)

@app.route("/profile")
def profile():
    #For looking at Height and Weight and how it affects players averages in the NBA
    return render_template("updatedprofile.html")

@app.route("/map")
def map():
    #Takes to the map page. Mapping the colleges on the map
    return render_template("map.html")

@app.route("/proposal")
def proposal():
    return render_template("proposal.html")

@app.route("/NBAData")
def NBAData():
    NBA = db.NBA
    docs = []
    for doc in NBA.find():
        doc.pop('_id') 
        docs.append(doc)
    return jsonify(docs)

@app.route("/NCAAData")
def NCAAData():
    NCAA = db.NCAA
    docs = []
    for doc in NCAA.find():
        doc.pop('_id') 
        docs.append(doc)
    return jsonify(docs)

@app.route("/NBALocation")
def NBALocation():
    NBA_Location = db.NBA_Location
    docs = []
    for doc in NBA_Location.find():
        doc.pop('_id') 
        docs.append(doc)
    return jsonify(docs)

@app.route("/Averages")
def Averages():
    schoolAverage = db.schoolAverage
    docs = []
    for doc in schoolAverage.find():
        doc.pop('_id') 
        docs.append(doc)
    return jsonify(docs)


if __name__ == "__main__":
    app.run(debug=True)
