import os
from flask import Flask, render_template,url_for
from app.api import app2

def create_app():
    app = Flask(__name__,static_folder="./app/static",template_folder="./app/templates")
    app.register_blueprint(app2)
    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index_url_for')
def index_url_for():
    return url_for('index')

if __name__ == '__main__':
    app.run()
