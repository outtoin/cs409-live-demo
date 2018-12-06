from flask import render_template, jsonify, request
from app import app

# Import the MLUtils
from ml_utils import MlUtils
mlu = MlUtils()

@app.route('/api/predict', methods=['POST'])
def api_predict():
    text = request.form.get('text')
    print(text)
    pred, fig = mlu.predict(text)
    return jsonify(pred)

@app.route('/api/top', methods=['GET'])
def api_top():
    num = request.args.get('num')
    data, path = mlu.make_top_list(int(num))
    return jsonify({'data': data, 'path':path})
