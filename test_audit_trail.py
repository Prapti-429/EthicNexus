import unittest
from audit_trail import AuditTrail
import os

class TestAuditTrail(unittest.TestCase):
    def setUp(self):
        self.trail = AuditTrail(log_file='test_audit_log.json')

    def tearDown(self):
        if os.path.exists('test_audit_log.json'):
            os.remove('test_audit_log.json')

    def test_log_decision(self):
        self.trail.log_decision('user123', ['label_A'], {'input': 'data'}, True)
        logs = self.trail.retrieve_logs()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0]['user_id'], 'user123')

if __name__ == '__main__':
    unittest.main()
