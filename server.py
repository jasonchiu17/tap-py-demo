import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api')
def api():
    resp = { 
    'data' : { 
        'd1': 'hello world',
        'd2': 'test'
    } ,
    'info' : { 
        'app_name' : 'TAP python demo',
        'data_from' : 'ZERONE'
        }
    }
    return jsonify(resp)

if __name__ == '__main__':
    app.run()
