import hashlib
from mongoengine import connect,disconnect,Document,StringField,SequenceField
from mongoengine.errors import NotUniqueError
from flask import Flask,request
import requests
# from pymongo import MongoClient

app=Flask(__name__)
connect(
    db='amit',
    host='127.0.0.1',
    port=27017
)
#disconnect(alias='project1')

class Comments(Document):
    name=StringField(required=True, unique=True, max_length=50)
    age=StringField(max_length=50)

class Member(Document):
    id=SequenceField(primary_key=True)
    membername=StringField(required=True, unique=True, max_length=50)

try:
    user=Comments(name='yellow')
    user.age='39'
    user.save()
except NotUniqueError:
    print('Name is not unique')
finally:
    disconnect(alias='default')
#start of pymong.Mongoclient
# client = MongoClient('localhost', 27017)
# db = client.amit #this is my database
# col = db.comments #this is my collection
# cur=col.find()  #this is cursor
# for doc in cur:
#     print(doc['name']+':'+doc['age'])
#db.comments.insert_one({'name':'Kunal', 'age':'30'})
#end of pymong.Mongoclient


data={1:{"name":"Amit","age":30},
2:{"name":"Ashu","age":29},
3:{"name":"Aman","age":28}
       }

@app.route("/person/<int:d>",methods=['GET'])
def gettestAPI(d):
    value=request.headers['x-verify']
    authkey = 'mysecretkey'
    str_forSha256 = 'mygeterequest' + authkey
    checksum = hashlib.sha256(str_forSha256.encode('UTF-8')).hexdigest()
    #print(checksum)
    if value!=checksum:
        return {'data':'Auth_failure'},401

    if d>3:
        return {},404
    return data[d]

@app.route("/member/<int:d>",methods=['GET'])
def getmemberAPI(d):
    connect(
        db='amit',
        host='127.0.0.1',
        port=27017
    )
    finalresp={}
    try:
        mem = Member.objects.get(id=d)
        finalresp['data']=mem.membername
    except Member.DoesNotExist:
        print('member does not exist')
        finalresp['data']='member does not exist'
    return finalresp

@app.route("/create",methods=['POST'])
def postAPI():
    connect(
        db='amit',
        host='127.0.0.1',
        port=27017
    )
    response=request.json
    finalresponse={}
    try:
        user = Comments(name=response['name'])
        user.age = response['age']
        user.save()

        #calling member API
        apiurl='http://127.0.0.1:5000/createmember/'+response['name']
        response=requests.post(url=apiurl)
        print(response.status_code)
        statuscode=response.status_code
        if statuscode==200:
            finalresponse['success']=True
        else:
            finalresponse['success']=False
    except NotUniqueError:
        print('Name is not unique')
        finalresponse['success']=False
        finalresponse['message']='Name is not unique'
    return finalresponse

@app.route("/createmember/<string:n>",methods=['POST'])
def postMemberAPI(n):
    finalresponse={}
    try:
        mem = Member(membername=n)
        mem.save()
        finalresponse['success']=True
    except NotUniqueError:
        print('Name is not unique')
        finalresponse['success']=False
        finalresponse['message']='Name is not unique'
    return finalresponse

@app.route("/member/<int:d>/<string:name>",methods=['PUT'])
def setmemberAPI(d,name):
    connect(
        db='amit',
        host='127.0.0.1',
        port=27017
    )
    finalresp={}
    try:
        mem = Member.objects.get(id=d)
        mem.update(membername=name)
        #after updating the name
        mem = Member.objects.get(id=d)
        finalresp['data']=mem.membername
    except Member.DoesNotExist:
        print('member does not exist')
        finalresp['data']='member does not exist'
    return finalresp

@app.route("/member/delete/<int:d>",methods=['POST'])
def removememberAPI(d):
    connect(
        db='amit',
        host='127.0.0.1',
        port=27017
    )
    finalresp={}
    try:
        mem = Member.objects.get(id=d)
        mem.delete()
        finalresp['data']='deleted'
    except Member.DoesNotExist:
        print('member does not exist')
        finalresp['data']='member does not exist'
    return finalresp

if __name__=='__main__':
    app.run(debug=True)