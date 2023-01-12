from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

posts = [
    {
        'author': 'Amit',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': '2nd May 2022'
    },
    {
        'author': 'Ashish',
        'title': 'Blog Post 2',
        'content': 'sec post content',
        'date_posted': '3rd May 2022'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route('/about')
def about():
    myname = 'Amit'
    return render_template('about.html', title='about', name=myname)


@app.route('/amit')
def amit():
    return "Amit Page"


@app.route('/amitJson')
def amitJson():
    # return jsonify(res="Amit Page")
    # return jsonify(e='Bad Request'),404
    return {'a': 'b'}


@app.route('/q_param/', methods=['GET'])
def getValueP():
    name = request.args.get("name")
    return jsonify(d=name)


# @app.route('/<string:name>')
# def getValue(name: str):
#     return jsonify(d=name)


if __name__ == "__main__":
    app.run(debug=True)
