import os
from flask_cors import CORS,cross_origin
from flask import Flask,request

#
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app,resource={r'/*':{'origins':'*'}})


@app.route('/')
@cross_origin()
def hello():
    return "hello world"

@app.route('/register',methods=['GET','POST'])
def register():
    from save_account import save_account
    data = request.data
    try:
        save_account(data)
        return data
    except Exception as e:
        return str(e),404
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')