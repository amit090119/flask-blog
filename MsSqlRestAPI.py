import hashlib
from mongoengine import connect,disconnect,Document,StringField,SequenceField
from mongoengine.errors import NotUniqueError
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,jsonify
import json
import requests
# from pymongo import MongoClient

app=Flask(__name__)
app.secret_key = 'amit-secret-key'

# related to sqlAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://mishra:Sweetpari121@mssql-103801-0.cloudclusters.net:10001/Employee"
db = SQLAlchemy(app)
print(db)

class Comments(db.Model):
    age = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)

# class Member(db.Model):
#     id=SequenceField(primary_key=True)
#     membername=StringField(required=True, unique=True, max_length=50)

@app.route('/')
@app.route('/index')
def index():
    ls=[]
    # posts = Comments.query.all()
    post=Comments.query.filter_by(name='Amit').first()
    print(type(post))
    print(post)
    return {post.name:post.age}

if __name__=='__main__':
    app.run(debug=True)