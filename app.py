from flask import Flask, request, jsonify
from audit_trail import AuditTrail
from ai_compliance import AIComplianceChecker
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
    """
    Endpoint to detect bias in AI predictions and check compliance with ethical standards.
    Accepts user ID and predictions as input, checks compliance, logs decisions, and returns status.
    """
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

    return jsonify({"compliance_status": compliant, "predictions": data['predictions']})


@app.route('/audit_logs', methods=['GET'])
def get_audit_logs():
    """
    Endpoint to retrieve audit logs.
    Logs include details of AI decisions and their compliance status.
    """
    logs = audit_trail.retrieve_logs()
    return jsonify({"logs": logs})


if __name__ == '__main__':
    # Run the app with debug mode on for easy troubleshooting during development
    app.run(debug=True)
