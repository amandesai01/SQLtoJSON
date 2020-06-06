from flask import Flask, request, jsonify
import json
import requests
from cruds.query import exec_query
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

if __name__ == "__main__":
    app.run(port = 4909, debug = True)