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
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("datapage.html")

@app.route("/data/<player>")
def dataplayer(player):
    return render_template("dataplayerpage.html", playername = player)

@app.route("/profile")
def profile():
    return render_template("updatedprofile.html")

@app.route("/NBAData")
def NBAData():
    NBA = db.NBA
    print(NBA.find_one())
    docs = []
    for doc in NBA.find():
        doc.pop('_id') 
        docs.append(doc)
    return jsonify(docs)

@app.route("/NCAAData")
def NCAAData():
    NCAA = db.NCAA
    print(NCAA.find_one())
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


if __name__ == "__main__":
    app.run(debug=True)
