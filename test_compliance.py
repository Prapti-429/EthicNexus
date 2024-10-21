import unittest
from ai_compliance import AIComplianceChecker

class TestAIComplianceChecker(unittest.TestCase):
    def setUp(self):
        ethical_standards = {
            'gender': {'prohibited_values': ['male', 'female']},
            'race': {'prohibited_values': ['white', 'black', 'asian']}
        }
        self.compliance_checker = AIComplianceChecker(ethical_standards)

    def test_compliance(self):
        input_data = {'gender': 'female', 'race': 'black'}
        compliance = self.compliance_checker.check_compliance([], input_data)
        self.assertFalse(compliance)

    def test_compliance_no_prohibited_values(self):
        input_data = {'gender': 'non_binary', 'race': 'latino'}
        compliance = self.compliance_checker.check_compliance([], input_data)
        self.assertTrue(compliance)

if __name__ == '__main__':
    unittest.main()
