from flask import Flask, render_template, session, url_for, redirect
import pickle
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

app = Flask(__name__)
app.secret_key = "KKKKEEEEYYY"
app.config['pickle'] = None
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

@app.route('/new', methods = ['POST', 'GET'])
def new():
    form = newConnForm()
    if form.is_submitted():
        s2jObj = pickle.dumps(app.config['pickle'])
        s2jObj.updateHost(form.host.data)
        s2jObj.updateUsername(form.username.data)
        s2jObj.updatePassword(form.password.data)
        s2jObj.updateDatabase(form.database.data)
        if s2jObj.checkConnection():
            return render_template('index.html')
        else:
            #restoring old version
            return render_template('newconnection.html', form = form, error=True)
    return render_template('newconnection.html', form = form, error=False)

@app.route('/querytab', methods=["POST", "GET"])
def querytab():
    if app.config['pickle']:
        s2jObj = pickle.loads(app.config['pickle'])
        form = queryForm()
        if form.is_submitted():
            query = form.Query.data
            resp = s2jObj.execQuery(query)
            return render_template('try_query.html', form=form, isRes=True, res=resp)
        return render_template('try_query.html', form=form, isRes=False, res="")
    else:
        return redirect(url_for('new'))

@app.route("/history")
def history():
    # print(s2jObj.get_history())
    if app.config['pickle']:
        s2jObj = pickle.loads(app.config['pickle'])
        return render_template('history.html', history = s2jObj.get_history())
    else:
        return redirect(url_for('new'))

@app.route("/")
def index():
    if app.config['pickle']:
        # print(s2jObj.get_history())
        return render_template('index.html')
    else:
        return redirect(url_for('new'))

def start(pick):
    app.config['pickle'] = pick
    if app.config['pickle']: # This means that object was successfully setuped in session.
        app.run(port=4001)

def update_pickle(pick):
    s2jObj = pickle.loads(pick)