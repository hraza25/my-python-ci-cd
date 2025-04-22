from flask import Flask
import os

app = Flask(__name__)

@app.route('/api')
def hello():
    return {"message": "Hello from Dockerized Python! Version 1.0"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
