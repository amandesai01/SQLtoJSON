from flask import Flask, render_template
import pickle

app = Flask(__name__)
# s2jObj = None


@app.route('/querytab')
def querytab():
    return "OK"

@app.route("/history")
def history():
    return "ok"

@app.route("/")
def index():
    # print(s2jObj.get_history())
    return render_template('index.html')

def start(pick):
    global s2jObj
    s2jObj = pickle.loads(pick)
    print(s2jObj)
    if s2jObj:
        app.run(port=4001)

def update_pickle(pick):
    s2jObj = pickle.loads(pick)