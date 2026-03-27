# cyber-project-01-log-analysis-suspicious-activity
Basic SOC log analysis to detect suspicious activity (brute force simulation)

📌 Context

In a real-world environment, Security Operations Center (SOC) analysts continuously monitor logs to detect suspicious activities. This project simulates a basic log analysis scenario to identify potential security threats.

🎯 Objective

* Understand log structures
* Detect suspicious behavior
* Identify brute force attack patterns

📂 Dataset

User: admin | IP: 192.168.1.10 | Status: SUCCESS
User: admin | IP: 45.33.32.1 | Status: FAILED
User: admin | IP: 45.33.32.1 | Status: FAILED
User: admin | IP: 45.33.32.1 | Status: FAILED
User: admin | IP: 45.33.32.1 | Status: SUCCESS


🔎 Analysis

* Multiple failed login attempts from the same IP address
* A successful login after several failures
  ➡️ This behavior strongly suggests a brute force attack

🚨 Conclusion

Suspicious IP identified: 45.33.32.1

Recommended actions:

* Block the IP address
* Enable Multi-Factor Authentication (MFA)
* Monitor account activity

📚 Key Takeaways

* How to read and interpret logs
* Detect brute force patterns
* Basic SOC analysis methodology

🚀 Future Improvements

* Automate detection using Python
* Integrate with SIEM tools
* Visualize log data

👨‍💻 Author

This project is part of my cybersecurity learning journey.
