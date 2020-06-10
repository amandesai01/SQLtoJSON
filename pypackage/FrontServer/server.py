from flask import Flask, render_template, redirect, url_for
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

@app.route('/new', methods = ['GET', 'POST'])
def new():
    form = newConnForm()
    if form.is_submitted():
        # backupS2JInstance =pickle.dumps(s2jObj)
        s2jObj.updateHost(form.host.data)
        s2jObj.updateUsername(form.username.data)
        s2jObj.updatePassword(form.password.data)
        s2jObj.updateDatabase(form.database.data)
        s2jObj.resetHistory()
        if s2jObj.checkConnection():
            return redirect(url_for('index'))
        else:
            #restoring old version
            # s2jObj = pickle.loads(backupS2JInstance)
            return render_template('newconnection.html', error=True, form=form)
    return render_template('newconnection.html', error=False, form=form)

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