class AIComplianceChecker:
    def __init__(self, ethical_standards):
        self.ethical_standards = ethical_standards

    def check_compliance(self, ai_decision, input_data):
        for key, value in self.ethical_standards.items():
            if key in input_data and input_data[key] in value['prohibited_values']:
                return False
        return True
