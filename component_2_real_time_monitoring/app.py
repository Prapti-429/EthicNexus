from flask import Flask, request, jsonify
from monitoring import log_decision
from bias_detection import detect_bias
from explanation import explain_decision

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_route():
    data = request.json['data']
    prediction = request.json['prediction']
    log_decision(data, prediction)
    return jsonify({"status": "logged"})

@app.route('/detect_bias', methods=['POST'])
def detect_bias_route():
    X = request.json['X']
    y = request.json['y']
    predictions = detect_bias(X, y)
    return jsonify({"predictions": predictions.tolist()})

@app.route('/explain', methods=['POST'])
def explain_route():
    data = request.json['data']
    explanation = explain_decision(data)
    return jsonify({"explanation": str(explanation)})

if __name__ == '__main__':
    app.run(debug=True)
