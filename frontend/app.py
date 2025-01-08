import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    backend_response = requests.get('http://backend-service:5000/api')
    return f"<h1>Frontend</h1><p>{backend_response.json().get('message')}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
