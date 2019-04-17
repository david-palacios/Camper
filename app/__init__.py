from flask import Flask, render_template, request
# from simplecrypt import encrypt, decrypt

app = Flask(__name__)

@app.route('/home')
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/home/map')
def getmap():
    apikey = "AIzaSyB31C7CeNH_CyGtLBaKz7SlWLmgkLvB7kE"
    return render_template('testGoogleAPI.html', key=apikey)


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

@app.route('/find')
def find():
    return render_template('find.html')
