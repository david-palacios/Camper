from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data = "data here")

@app.route('/getData', methods=['GET'])
def getData():
    if request.method == 'GET':
        return render_template('getData.html', data=request.args.get('data'))
    else:
        return "404"

@app.route('/getData/<num>', methods=['GET'])
def getData2(num):
    if request.method == 'GET':
        return render_template('getData.html', data=num)
    else:
        return "404"

@app.route('/postForm')
def postForm():
    return render_template('postForm.html')