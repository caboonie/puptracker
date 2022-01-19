from database import *
from flask import Flask, request, redirect, render_template, Response, send_file, url_for, flash
from flask import session as login_session
import json
from functools import wraps
from datetime import datetime, timedelta 

app = Flask(__name__)
app.config['SECRET_KEY'] = "a;lfkdsjaflksdj"

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html", note_types=get_note_types(), 
            notes= sorted(get_notes(), key=lambda x:x.time, reverse=True))

@app.route('/quick_add/<int:type_id>')
def quick_add(type_id):
    create_note(type_id, datetime.now()-timedelta(hours=5), "")
    return redirect(url_for("home"))



if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
