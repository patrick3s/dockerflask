import os

from flask import Flask,request

#
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/register',methods=['GET','POST'])
def register():
    data = request.data
    return data,200
if __name__ == "__main__":
    app.run(host='0.0.0.0')