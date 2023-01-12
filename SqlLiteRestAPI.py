from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,jsonify
import json
import requests

app=Flask(__name__)
app.secret_key = 'amit-secret-key'

# related to sqlAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
print(db)

class Emp(db.Model):
    age = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)

# class Member(db.Model):
#     id=SequenceField(primary_key=True)
#     membername=StringField(required=True, unique=True, max_length=50)

@app.route('/')
@app.route('/index')
def index():
    # posts = Comments.query.all()
    post=Emp.query.filter_by(name='Aman').first()
    print(type(post))
    print(post)
    return {post.name:post.age}

@app.route('/add')
def addEmp():
    post = Emp(name='Aman', age=29)
    db.session.add(post)
    db.session.commit()
    return {post.name:post.age}

if __name__=='__main__':
    app.run(debug=True)
    db.create_all()