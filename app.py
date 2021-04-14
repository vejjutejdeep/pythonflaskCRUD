import os
from flask import Flask, session, render_template, request, redirect, url_for, jsonify
from flask_session import Session
# from flask_mongoengine import MongoEngine
# import json
import pymongo
from bson import ObjectId

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config.from_object(__name__)
Session(app)

app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'flaskproduct',
#     'host': 'mongodb+srv://star:rh65kq@cluster0.qnu5u.mongodb.net/flaskproduct?retryWrites=true&w=majority'
# }

# db = MongoEngine()

myclient = pymongo.MongoClient("mongodb+srv://star:rh65kq@cluster0.qnu5u.mongodb.net/flaskproduct?retryWrites=true&w=majority")
mydb = myclient["flaskproduct"]
mycol = mydb["product"]

# db.init_app(app)
@app.route("/", methods=["GET"])
def veiw():
    data = ""
    for x in mycol.find():
        data += str(x)
    return data

@app.route("/addproduct", methods=["POST"])
def addproduct():
    request_data = request.get_json()
    # print("data",request_data)
    name = request_data['productname']
    cost = request_data['cost']
    mydict = { "product name": name, "cost": cost }
    x = mycol.insert_one(mydict)
    return (str(x) + "created object in the DB")

@app.route("/deleteproduct", methods=["DELETE"])
def deleteproduct():
    productid = request.args.get('productid')

    myquery = { "_id": ObjectId(productid) }

    mycol.delete_one(myquery)

    return "the object is deleted."

@app.route("/updateproduct", methods=["PATCH"])
def updateproduct():
    request_data = request.get_json()
    idval = request.args.get('productid')

    myquery = {"_id" : ObjectId(idval)}
    newvalues = {"$set": request_data}
    x = mycol.update_many(myquery, newvalues)
    return "value is updated."