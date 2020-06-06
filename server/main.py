from flask import Flask, request, jsonify
import json
import requests
from cruds import query
app = Flask(__name__)

@app.route('/execQuery')
def execQuery():
    database = request.args.get('database')
    host = request.args.get('host')
    username = request.args.get('username')
    password = request.args.get('password')
    try:
        return jsonify(query.execQuery(database, host, username, password))
    except Exception as e:
        return jsonify({ "status" : "failure", "error" : str(e) })

if __name__ == "__main__":
    app.run(port = 4909, debug = True)