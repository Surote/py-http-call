from flask import Flask,render_template
import requests
import json
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def home():
    api_url = str(os.getenv("api_endpoint","localhost:8080"))
    headers = {'local_service': 'call from py-reader'}
    response = requests.get('http://'+api_url,headers=headers)

    if response.status_code == 200:
        # If the request was successful, parse the JSON response
        data = response.json()

        background_color = os.environ.get("BACKGROUND_COLOR", "blue")

        # Render an HTML template with the background color
        return render_template('home.html', json_data=json.dumps(data, indent=4), background_color=background_color)
        #return data
    else:
        # If the request was not successful, return an error message
        return "{'Error'}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)