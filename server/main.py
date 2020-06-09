from flask import Flask, request, jsonify
import json
import requests
from cruds.query import exec_query, checkConnection
app = Flask(__name__)

@app.route('/execQuery', methods = ["POST", "GET"])
def execQuery():
    data = request.get_json()
    database = data.get('database')
    host = data.get('host')
    username = data.get('username')
    password = data.get('password')
    query = data.get('query')
    print(database, username, password, host)
    try:
        return jsonify(exec_query(query, database, host, username, password))
    except Exception as e:
        return jsonify({ "status" : "failure", "error_message" : str(e) })

@app.route('/check')
def check():
    data = request.get_json()
    database = data.get('database')
    host = data.get('host')
    username = data.get('username')
    password = data.get('password')
    if checkConnection(database, host, username, password):
        return jsonify({"status" : "ok"})
    return jsonify({"status" : "failure"})

if __name__ == "__main__":
    app.run(port = 4909, debug = True)