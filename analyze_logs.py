# 🔍 Log Analysis Script - Suspicious Activity Detection

logs = [
    "User: admin | IP: 192.168.1.10 | Status: SUCCESS",
    "User: admin | IP: 45.33.32.1 | Status: FAILED",
    "User: admin | IP: 45.33.32.1 | Status: FAILED",
    "User: admin | IP: 45.33.32.1 | Status: FAILED",
    "User: admin | IP: 45.33.32.1 | Status: SUCCESS"
]

# Dictionary to store IP activity
ip_attempts = {}

# Process logs
for log in logs:
    parts = log.split("|")
    ip = parts[1].split(":")[1].strip()
    status = parts[2].split(":")[1].strip()

    # Initialize dictionary if IP not seen before
    if ip not in ip_attempts:
        ip_attempts[ip] = {"FAILED": 0, "SUCCESS": 0}

    # Count attempts
    ip_attempts[ip][status] += 1

# Generate report
print("=== Log Analysis Report ===\n")

for ip, data in ip_attempts.items():
    print(f"IP Address: {ip}")
    print(f"Failed attempts: {data['FAILED']}")
    print(f"Successful attempts: {data['SUCCESS']}\n")

    # Detection rule
    if data["FAILED"] >= 3:
        print(f"[ALERT] Suspicious activity detected from {ip}\n")
