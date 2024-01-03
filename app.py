from flask import Flask,render_template,request
import requests
import json
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def home():
    api_url = str(os.getenv("api_endpoint","localhost:8081/api/v1"))
    headers = { 'local_service': 'call from py-reader',
                'X-B3-Traceid': str(request.headers.get('X-B3-Traceid')),
                'X-B3-Spanid': str(request.headers.get('X-B3-Spanid')),
                'X-B3-Parentspanid': str(request.headers.get('X-B3-Parentspanid'))
    }
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
        return "Header return not 200"

@app.route('/api/v1')
def local_api():
    data = {'data': 'Cannot find correct env api_endpoint'}
    return json.dumps(data),200

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)
