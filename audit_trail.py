import json
import datetime

class AuditTrail:
    def __init__(self, log_file='audit_log.json'):
        self.log_file = log_file

    def log_decision(self, user_id, ai_decision, input_data, compliance_status):
        log_entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'user_id': user_id,
            'input_data': input_data,
            'ai_decision': ai_decision,
            'compliance_status': compliance_status
        }
        self._write_log(log_entry)

    def _write_log(self, entry):
        with open(self.log_file, 'a') as log:
            log.write(json.dumps(entry) + "\n")

    def retrieve_logs(self):
        logs = []
        try:
            with open(self.log_file, 'r') as log:
                logs = [json.loads(line) for line in log]
        except IOError:
            print("No logs found.")
        return logs
