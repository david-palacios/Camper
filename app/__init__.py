from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/home')
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data = "data here")

@app.route('/home/map')
def getmap():
    return render_template('testGoogleAPI.html')

@app.route('/getdata', methods=['GET'])
def getdata():
    if request.method == 'GET':
        return render_template('getData.html', data=request.args.get('data'))
    else:
        return "404"


@app.route('/getdata/<num>', methods=['GET'])
def getdata2(num):
    if request.method == 'GET':
        return render_template('getData.html', data=num)
    else:
        return "404"


@app.route('/postform')
def postform():
    return render_template('postForm.html')