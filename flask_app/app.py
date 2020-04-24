from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello,World!!!"

@app.route('/david')
def david():
     return 'hello, david!'


@app.route('/adrian')
def adrian():
    return '<h1>test</h1>'

@app.route('/test')
def test():
    return render_template('index.html')
