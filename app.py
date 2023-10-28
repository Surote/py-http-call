from flask import Flask,request
import requests
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def home():
    api_url = str(os.getenv("api_endpoint","localhost"))
    headers = {'local_service': 'call from py-reader'}
    response = requests.get('http://'+api_url,headers=headers)

    if response.status_code == 200:
        # If the request was successful, parse the JSON response
        data = response.json()
        return data
    else:
        # If the request was not successful, return an error message
        return "{'Error'}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)