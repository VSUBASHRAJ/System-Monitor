import psutil
import datetime
import os

# Absolute paths (important for cron)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "system.log")
ALERT_FILE = os.path.join(LOG_DIR, "alerts.log")

# Ensure logs folder exists
os.makedirs(LOG_DIR, exist_ok=True)

CPU_THRESHOLD = 80  # Alert threshold

try:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.datetime.now()

    log_data = f"{timestamp} | CPU: {cpu}% | MEM: {memory}% | DISK: {disk}%\n"

    # Write normal log
    with open(LOG_FILE, "a") as f:
        f.write(log_data)

    print("✅ Logged:", log_data)

    # 🚨 ALERT CONDITION
    if cpu > CPU_THRESHOLD:
        alert_msg = f"{timestamp} | 🚨 HIGH CPU ALERT: {cpu}%\n"

        # Save alert
        with open(ALERT_FILE, "a") as f:
            f.write(alert_msg)

        print(alert_msg)

except Exception as e:
    error_log = f"{datetime.datetime.now()} | ERROR: {str(e)}\n"
    with open(LOG_FILE, "a") as f:
        f.write(error_log)