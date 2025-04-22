from flask import Flask
import os

app = Flask(__name__)

@app.route('/api')
def hello():
    return {"message": "Hello from Dockerized Python! Version 2.0, A fully functional ci-cd pipeline which updates code to docker hub"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
