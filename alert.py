import psutil

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent




if cpu > 80:
    print("⚠️ High CPU Usage!")

if memory > 80:
    print("⚠️ High Memory Usage!")

if cpu <= 80 and memory <= 80:
    print("✅ System is stable")