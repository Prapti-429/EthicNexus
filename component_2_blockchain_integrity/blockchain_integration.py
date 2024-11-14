from web3 import Web3
import json
from cryptography.fernet import Fernet
import base64

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Contract details
contract_address = "0x859Ce59ceC7cac63fdC98C5ccc84Ac6bE3754e62"  # Replace with your actual contract address
with open('build/contracts/DataAuditTrail.json') as f:
    contract_abi = json.load(f)['abi']

contract = w3.eth.contract(address=contract_address, abi=contract_abi)
account = w3.eth.accounts[0]

# Encryption setup
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

def log_data_on_blockchain(data):
    """Encrypts and logs data on the blockchain for privacy."""
    print("Logging data to blockchain:", data)  # Debug print
    encrypted_data = cipher_suite.encrypt(data.encode())
    # Encode encrypted data to Base64 string
    encoded_data = base64.b64encode(encrypted_data).decode('utf-8')
    tx = contract.functions.storeData(encoded_data).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx)
    print("Data logged on blockchain successfully.")

def audit_log_action(action, details):
    """Logs an action with details immutably on the blockchain for accountability."""
    log_entry = f"Action: {action}, Details: {details}"
    print("Audit log action:", log_entry)  # Debug print
    encrypted_log = cipher_suite.encrypt(log_entry.encode())
    # Encode encrypted log to Base64 string
    encoded_log = base64.b64encode(encrypted_log).decode('utf-8')
    tx = contract.functions.storeLog(encoded_log).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx)
    print("Audit log stored on blockchain successfully.")
