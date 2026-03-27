logs = [
    "User: admin | IP: 192.168.1.10 | Status: SUCCESS",
    "User: admin | IP: 45.33.32.1 | Status: FAILED",
    "User: admin | IP: 45.33.32.1 | Status: FAILED",
    "User: admin | IP: 45.33.32.1 | Status: FAILED",
    "User: admin | IP: 45.33.32.1 | Status: SUCCESS"
]

ip_attempts = {}

for log in logs:
    parts = log.split("|")
    ip = parts[1].split(":")[1].strip()
    status = parts[2].split(":")[1].strip()

    if ip not in ip_attempts:
        ip_attempts[ip] = {"FAILED": 0, "SUCCESS": 0}

    ip_attempts[ip][status] += 1

print("=== Log Analysis Report ===\n")

for ip, data in ip_attempts.items():
    print(f"IP Address: {ip}")
    print(f"Failed attempts: {data['FAILED']}")
    print(f"Successful attempts: {data['SUCCESS']}\n")

    if data["FAILED"] >= 3:
        print(f"[ALERT] Suspicious activity detected from {ip}\n")
