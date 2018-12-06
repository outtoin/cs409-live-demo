from flask import render_template, jsonify
from app import app

@app.route('/')
@app.route('/viewer')
def viewer():
    return render_template('index2.html', title='Viewer')