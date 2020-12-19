"""Ingest the deadside death log"""

import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import pandas
import data_ops

UPLOAD_FOLDER = '../files'
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"
app.config['UPLOAD_FOLDER'] = '../files'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/ingest", methods=['GET', 'POST'])
def ingest():
    if request.method == 'POST':
        f = request.files['filename']
        # f.save(f"{app.config['UPLOAD_FOLDER']}/deadside_data.csv")
        with open(f"{app.config['UPLOAD_FOLDER']}/deadside_data.csv", "ab") as stats:
            stats.write(f.read())
        return render_template('upload_ok.html')
    return render_template('ingest.html')

@app.route("/")
def maindisplay():

    return data_ops.marksman_award()


if __name__ == "__main__":
    app.run()
