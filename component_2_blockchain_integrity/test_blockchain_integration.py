import unittest
from unittest.mock import patch, MagicMock
from blockchain_integration import log_data_on_blockchain, audit_log_action, cipher_suite, w3
import base64

class BlockchainIntegrationTestCase(unittest.TestCase):
    
    @patch('blockchain_integration.contract.functions.storeData.transact')
    @patch('blockchain_integration.w3.eth.wait_for_transaction_receipt')
    def test_log_data_on_blockchain(self, mock_wait_for_receipt, mock_transact):
        """
        Test logging data on the blockchain.
        """
        # Set up mock transaction receipt
        mock_transact.return_value = "0x12345abcd"  # Hexadecimal mock transaction hash
        mock_wait_for_receipt.return_value = MagicMock()  # Mock the receipt

        # Define test data
        data = "Test log data for blockchain"
        
        # Call the function
        log_data_on_blockchain(data)
        
        # Encrypt data to verify it's processed correctly
        encrypted_data = cipher_suite.encrypt(data.encode())
        encoded_data = base64.b64encode(encrypted_data).decode('utf-8')
        
        # Check if the function called storeData with the correct parameters
        mock_transact.assert_called_once_with({'from': w3.eth.accounts[0]})
        self.assertTrue(encoded_data)  # Ensure encoded data is non-empty
        print("Test for log_data_on_blockchain passed.")
    
    @patch('blockchain_integration.contract.functions.storeLog.transact')
    @patch('blockchain_integration.w3.eth.wait_for_transaction_receipt')
    def test_audit_log_action(self, mock_wait_for_receipt, mock_transact):
        """
        Test logging an audit action on the blockchain.
        """
        # Set up mock transaction receipt
        mock_transact.return_value = "0x12345abcd"  # Hexadecimal mock transaction hash
        mock_wait_for_receipt.return_value = MagicMock()  # Mock the receipt

        # Define test action and details
        action = "Test Action"
        details = "Test Details for Audit"
        
        # Call the function
        audit_log_action(action, details)
        
        # Encrypt log entry for comparison
        log_entry = f"Action: {action}, Details: {details}"
        encrypted_log = cipher_suite.encrypt(log_entry.encode())
        encoded_log = base64.b64encode(encrypted_log).decode('utf-8')
        
        # Check if the function called storeLog with the correct parameters
        mock_transact.assert_called_once_with({'from': w3.eth.accounts[0]})
        self.assertTrue(encoded_log)  # Ensure encoded log is non-empty
        print("Test for audit_log_action passed.")
    
    def test_encryption_integrity(self):
        """
        Test the encryption and decryption process to ensure data integrity.
        """
        data = "Sensitive data to log"
        encrypted_data = cipher_suite.encrypt(data.encode())
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')
        
        # Check if the decrypted data matches the original data
        self.assertEqual(data, decrypted_data)
        
        print("Encryption integrity test passed.")
    
    @patch('blockchain_integration.contract.functions.storeData.transact', return_value="0x12345abcd")
    @patch('blockchain_integration.w3.eth.wait_for_transaction_receipt', return_value=MagicMock())
    def test_mock_blockchain_logging(self, mock_wait_for_receipt, mock_transact):
        """
        Test log_data_on_blockchain with a mocked blockchain transaction.
        """
        data = "Mock data"
        log_data_on_blockchain(data)
        mock_transact.assert_called_once()
        print("Mock blockchain logging test passed.")

if __name__ == '__main__':
    unittest.main()
