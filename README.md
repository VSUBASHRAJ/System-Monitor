# System Monitoring and Alerting Tool

A lightweight DevOps-focused project that monitors system resources and triggers alerts when CPU usage exceeds a defined threshold. This project demonstrates Linux automation, Python scripting, and real-time system monitoring concepts.

---

## Features

* Monitors CPU, memory, and disk usage
* Automated execution using Linux cron jobs
* Threshold-based alert system (CPU usage above 80%)
* Generates structured logs for system activity and alerts
* Uses Python for scripting and automation
* Runs in a Linux environment (WSL)

---

## Tech Stack

* Python (psutil)
* Linux (WSL)
* Cron jobs
* Git and GitHub

---

## Project Structure

system-monitor/
│── monitor.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── logs/
│   ├── system.log
│   ├── alerts.log
│   └── cron.log
│
├── scripts/
│   └── run.sh

---

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/VSUBASHRAJ/System-Monitor.git
cd system-monitor

---

### 2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

---

### 3. Run the Application

python monitor.py

---

### 4. Setup Cron Job

crontab -e

Add the following line:

*/1 * * * * /path/to/venv/bin/python /path/to/system-monitor/monitor.py >> /path/to/system-monitor/logs/cron.log 2>&1

---

## Sample Output

system.log
2026-04-10 16:30:10 | CPU: 45% | MEM: 60% | DISK: 30%

alerts.log
2026-04-10 16:32:10 | HIGH CPU ALERT: 92%

---

## Use Case

This project simulates a real-world monitoring system used in DevOps environments to track system performance and detect abnormal resource usage.

---
Screenshots:


## Key Learnings

* Automating tasks using Linux cron jobs
* Writing Python scripts for system monitoring
* Managing dependencies using virtual environments
* Debugging cron execution issues using logs
* Implementing threshold-based alerting

---

## Future Improvements

* Email or messaging alerts
* Containerization using Docker
* Web-based dashboard for monitoring

---

## Author

Subash Raj
