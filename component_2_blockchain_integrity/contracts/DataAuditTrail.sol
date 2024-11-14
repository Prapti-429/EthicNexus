// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataAuditTrail {
    // Struct to hold data entries
    struct DataEntry {
        address user;
        string encryptedData;
        uint256 timestamp;
    }

    // Struct to hold log entries
    struct LogEntry {
        address user;
        string encryptedLog;
        uint256 timestamp;
    }

    // Arrays to store data entries and audit logs
    DataEntry[] public dataEntries;
    LogEntry[] public logEntries;

    // Event to notify when data is stored
    event DataStored(address indexed user, string encryptedData, uint256 timestamp);

    // Event to notify when a log is stored
    event LogStored(address indexed user, string encryptedLog, uint256 timestamp);

    // Function to store encrypted data
    function storeData(string memory _encryptedData) public {
        DataEntry memory newData = DataEntry({
            user: msg.sender,
            encryptedData: _encryptedData,
            timestamp: block.timestamp
        });
        dataEntries.push(newData);
        emit DataStored(msg.sender, _encryptedData, block.timestamp);
    }

    // Function to store encrypted log entries
    function storeLog(string memory _encryptedLog) public {
        LogEntry memory newLog = LogEntry({
            user: msg.sender,
            encryptedLog: _encryptedLog,
            timestamp: block.timestamp
        });
        logEntries.push(newLog);
        emit LogStored(msg.sender, _encryptedLog, block.timestamp);
    }

    // Function to get all data entries
    function getDataEntries() public view returns (DataEntry[] memory) {
        return dataEntries;
    }

    // Function to get all log entries
    function getLogEntries() public view returns (LogEntry[] memory) {
        return logEntries;
    }
}
