import random
from datetime import datetime, timedelta
import os

MODULES = ["Auth", "DB", "Network", "UI", "Scheduler"]
SEVERITIES = ["INFO", "WARNING", "ERROR"]
EVENT_CODES = {
    "INFO": ["I100", "I101", "I102"],
    "WARNING": ["W200", "W201", "W202"],
    "ERROR": ["E300", "E301", "E302"]
}
MESSAGES = {
    "Auth": ["Login success", "Logout", "Password changed", "Failed login attempt"],
    "DB": ["Query executed", "Connection timeout", "Transaction rolled back", "Connection established"],
    "Network": ["Packet sent", "Packet dropped", "Latency high", "Connection lost"],
    "UI": ["Button clicked", "Page loaded", "Render delay", "UI error"],
    "Scheduler": ["Job executed", "Job failed", "Job delayed", "Job queued"]
}

def generate_logs(filepath, num_events=500):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    start_time = datetime.now() - timedelta(hours=5)
    with open(filepath, "w") as f:
        for _ in range(num_events):
            module = random.choice(MODULES)
            severity = random.choices(SEVERITIES, weights=[0.7, 0.2, 0.1])[0]
            code = random.choice(EVENT_CODES[severity])
            message = random.choice(MESSAGES[module])
            timestamp = start_time + timedelta(seconds=random.randint(0, 18000))
            line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {module} | {severity} | {code} | {message}\n"
            f.write(line)
