from flask import Flask, request, jsonify
import json
import requests
from cruds import query
app = Flask(__name__)

@app.route('/dumpcreds', methods = ['GET'])
def dumpCreds():
    cred = {}
    url = request.args.get('url')
    port = request.args.get('port')
    username = request.args.get('username')
    password = request.args.get('password')
    if url is None or port is None or username is None or password is None:
        return jsonify({"status" : "error"})
    cred['url'] = url
    cred['port'] = port
    cred['username'] = username
    cred['password'] = password
    
    try:
        with open('config.json', 'w') as fp:
            try:
                json.dump(cred, fp, indent=4)
                return jsonify({"status" : "ok"})
            except Exception as e:
                return jsonify({"status" : "error"})
    except:
        return jsonify({"status" : "error"})
    
@app.route('/checkcreds')
def checkCreds():
    try:
        with open('config.json', 'r') as fp:
            data = json.load(fp)
            data['status'] = "ok"
            return jsonify(data)
    except:
        return jsonify({ 'status': 'error' })

@app.route('/execQuery')
def execQuery():
    database = request.args.get('database')
    response = {}
    creds = {}
    try:
        with open('config.json', 'r') as fp:
            creds = json.load(fp)
    except:
        response['status'] = 'error'
        return jsonify(response)
    return query.execQuery()

if __name__ == "__main__":
    app.run(debug = True)