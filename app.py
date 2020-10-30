from flask import (Flask, g, render_template, flash, redirect, url_for, 
                  abort)


DEBUG = True
PORT = 8000
HOST = '127.0.0.1'

app = Flask(__name__)
app.secret_key = ':/}*vZ+Py-67]tA^ng53gf~XmQ76z]'

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)