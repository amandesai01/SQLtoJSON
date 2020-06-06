from flask import Flask, request, jsonify
import json
import requests
from cruds import query
app = Flask(__name__)

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