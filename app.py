"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request, Response
import json
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/', methods=['POST', 'GET'])
def practice():
    Username = request.values['Username']
    Password = request.values['Password']
    print(Username, Password)
    if Username == "user1" and Password == "0000":
        result = {
            'r' : 0,
            'm' : "success"
            }
        return Response(json.dumps(result), mimetype='application/json')
    else :
        result = {
            'r' : 1,
            'm' : "failure"
            }
    return Response(json.dumps(result), mimetype='application/json')
    

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run('0.0.0.0', PORT, debug=True)
