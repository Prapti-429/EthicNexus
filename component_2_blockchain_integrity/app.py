from flask import Flask, request, jsonify, render_template
from audit_trail import AuditTrail
from ai_compliance import AIComplianceChecker
from blockchain_integration import log_data_on_blockchain, audit_log_action  # Import blockchain functions
import pandas as pd

app = Flask(__name__)

audit_trail = AuditTrail()
ethical_standards = {
    'gender': {'prohibited_values': ['male', 'female']},
    'race': {'prohibited_values': ['white', 'black', 'asian']}
}
compliance_checker = AIComplianceChecker(ethical_standards)

@app.route('/detect_bias', methods=['POST'])
def detect_bias():
    data = request.get_json()
    user_id = data.get('user_id')
    
    # Ensure predictions are provided in the correct format
    if 'predictions' not in data:
        return jsonify({"error": "Missing 'predictions' in request data"}), 400
    
    predictions_df = pd.DataFrame(data['predictions'])

    # Check AI compliance with the ethical standards
    compliant = compliance_checker.check_compliance([], data['predictions'])
    
    # Log the decision in the audit trail
    audit_trail.log_decision(user_id, [], data['predictions'], compliant)

    # Log decision on blockchain
    log_data = f"UserID: {user_id}, Predictions: {data['predictions']}, Compliant: {compliant}"
    log_data_on_blockchain(log_data)  # This logs the data on blockchain

    # Use audit_log_action for logging an action
    action = "Bias Detection"
    details = f"Compliance check for user_id {user_id} with result: {compliant}"
    audit_log_action(action, details)  # Logs the action on the blockchain

    return jsonify({"compliance_status": compliant, "predictions": data['predictions']})


@app.route('/audit_logs', methods=['GET'])
def get_audit_logs():
    """
    Endpoint to retrieve audit logs.
    Logs include details of AI decisions and their compliance status.
    """
    logs = audit_trail.retrieve_logs()
    return jsonify({"logs": logs})

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    # Run the app with debug mode on for easy troubleshooting during development
    app.run(debug=True)

