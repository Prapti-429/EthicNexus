// Function to log data on blockchain
async function logDataOnBlockchain(data) {
  try {
    const response = await fetch("/log_data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ data: data }),
    });

    const result = await response.json();
    alert(result.message || result.error);
  } catch (error) {
    console.error("Error logging data:", error);
  }
}

// Function to audit log an action on the blockchain
async function auditLogAction(action, details) {
  try {
    const response = await fetch("/audit_log", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ action: action, details: details }),
    });

    const result = await response.json();
    alert(result.message || result.error);
  } catch (error) {
    console.error("Error logging action:", error);
  }
}

// Example function to add a decision block to the UI
function addDecisionToList(title, description) {
  const decisionsList = document.getElementById("decisions-list");
  const decisionItem = document.createElement("li");
  decisionItem.innerHTML = `
      <div class="decision-block">
        <h3 class="decision-title">${title}</h3>
        <p class="decision-description">${description}</p>
      </div>
    `;
  decisionsList.appendChild(decisionItem);
}

// Sample event listener (you can add buttons to trigger these)
document.addEventListener("DOMContentLoaded", () => {
  // Example data logging
  document.getElementById("logDataButton").addEventListener("click", () => {
    logDataOnBlockchain("Sample data for blockchain");
  });

  // Example action logging
  document.getElementById("auditLogButton").addEventListener("click", () => {
    auditLogAction("Sample Action", "Sample Details");
  });
});

async function fetchAuditLogs() {
  try {
    const response = await fetch("/audit_logs");
    const data = await response.json();

    const decisionsList = document.getElementById("decisions-list");
    decisionsList.innerHTML = ""; // Clear existing content

    data.logs.forEach((log) => {
      const decisionItem = document.createElement("li");
      decisionItem.innerHTML = `
        <div class="decision-block">
          <h3 class="decision-title">User ID: ${log.user_id}</h3>
          <p class="decision-description">Compliance Status: ${
            log.compliance_status
          }</p>
          <p class="decision-description">Details: ${JSON.stringify(
            log.details
          )}</p>
        </div>
      `;
      decisionsList.appendChild(decisionItem);
    });
  } catch (error) {
    console.error("Error fetching audit logs:", error);
  }
}

// Fetch audit logs when the page loads
document.addEventListener("DOMContentLoaded", fetchAuditLogs);
