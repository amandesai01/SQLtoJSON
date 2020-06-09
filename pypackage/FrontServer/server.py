from flask import Flask, render_template
import pickle
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

app = Flask(__name__)
app.secret_key = "KKKKEEEEYYY"
# s2jObj = None
class queryForm(FlaskForm):
    Query = StringField()
    Submit = SubmitField('Run')

class newConnForm(FlaskForm):
    host = StringField()
    username = StringField()
    password = PasswordField()
    database = StringField()
    connect = SubmitField('Connect')

@app.route('/querytab', methods=["POST", "GET"])
def querytab():
    form = queryForm()
    if form.is_submitted():
        query = form.Query.data
        resp = s2jObj.execQuery(query)
        return render_template('try_query.html', form=form, isRes=True, res=resp)
    return render_template('try_query.html', form=form, isRes=False, res="")

@app.route("/history")
def history():
    # print(s2jObj.get_history())
    return render_template('history.html', history = s2jObj.get_history())

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