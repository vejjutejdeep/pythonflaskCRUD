import os
from flask import Flask, session, render_template, request, redirect, url_for, jsonify
from flask_session import Session
# from flask_mongoengine import MongoEngine
# import json
import pymongo

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

db.init_app(app)
@app.route("/", methods=["GET"])
def veiw():
    return "under construction"

@app.route("/addproduct", methods=["POST"])
def addproduct:


