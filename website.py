from flask import Flask, render_template, jsonify, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import json

with open('config.json', 'r') as f:
    param = json.load(f)

app = Flask(__name__)
app.secret_key = 'amit-secret-key'

# related to sqlAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
uri = param["params"]["local_uri"]
app.config['SQLALCHEMY_DATABASE_URI'] = uri
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Flaskdatabase'
db = SQLAlchemy(app)

# related to flask-mail
app.config.update(
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=param['params']['gmail-username'],
    MAIL_PASSWORD=param['params']['gmail-password'],
    MAIL_SERVER='smtp.gmail.com',
    MAIL_USE_TLS=False
)

mail = Mail(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    date = db.Column(db.String(20), unique=True, nullable=False)
    mob = db.Column(db.String(10), unique=True, nullable=True)
    msg = db.Column(db.String(50), unique=True, nullable=False)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(50), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.String(20), unique=True, nullable=False)


@app.route('/')
@app.route('/index')
def index():
    posts = Posts.query.filter_by().all()
    return render_template('index.html', param=param, posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', param=param)


@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', param=param, post=post)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session and session['user'] == param["params"]["login-username"]:
        posts = Posts.query.all()
        return render_template('dashboard.html', param=param, posts=posts)

    if request.method == 'POST':
        username = request.form.get('uname')
        passwrd = request.form.get('pwd')

        if username == param["params"]["login-username"] and passwrd == param["params"]["login-pass"]:
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', param=param, posts=posts)
    return render_template('login.html', param=param)

@app.route('/logout')
def logout():
    if 'user' in session and session['user'] == param["params"]["login-username"]:
        session.pop('user')
    return render_template('login.html', param=param)

@app.route('/delete/<string:sno>', methods=['GET', 'POST'])
def deletePost(sno):
    if 'user' in session and session['user'] == param["params"]["login-username"]:
        post=Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/login')

@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def editPost(sno):
    if 'user' in session and session['user'] == param["params"]["login-username"]:
        if request.method == 'POST':
            title = request.form.get('title')
            slug = request.form.get('slug')
            content = request.form.get('content')
            if sno=='0':
                post=Posts(title=title,slug=slug,content=content,date=datetime.now())
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title=title
                post.slug=slug
                post.content=content
                post.date=datetime.now()
                db.session.commit()
                return redirect('/edit/'+sno)
    post = Posts.query.filter_by(sno=sno).first()
    return render_template('editPost.html', param=param, post=post, sno=sno)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        emailid = request.form.get('email')
        mobile = request.form.get('mob')
        msg = request.form.get('msg')
        entry = Contacts(name=name, email=emailid, mob=mobile, msg=msg, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from '+ name,
        #                   sender=emailid,
        #                   recipients=[param['params']['gmail-username']],
        #                   body= msg+ "\n" + mobile
        #                   )
    return render_template('contact.html', param=param)


if __name__ == "__main__":
    app.run(debug=True)
