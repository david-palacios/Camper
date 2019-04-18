from flask import Flask, render_template, request
import os

from Crypto.Cipher import XOR
import base64

app = Flask(__name__)

#app.config['SERVER_NAME'] = 'TreeLine'


def encrypt(key, plaintext):
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(plaintext))


def decrypt(key, ciphertext):
    cipher = XOR.new(key)
    return cipher.decrypt(base64.b64decode(ciphertext))


@app.route('/home')
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/home/map')
def getmap():
    apikey = open("./res/key.txt")
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
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    key = open(curr_dir + "/res/key.txt").read()

    # encripted = encrypt(open(curr_dir+"/res/key.txt").read(), "AIzaSyB31C7CeNH_CyGtLBaKz7SlWLmgkLvB7kE")
    # write = open(curr_dir+"/res/encrypted.txt", "wb")
    # write.write(encripted)
    # write.close()

    apikey = decrypt(key, open(curr_dir + "/res/encrypted.txt", "rb").read()).decode("utf-8")

    return render_template('find.html', key=apikey)
