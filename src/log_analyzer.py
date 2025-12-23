import os
from collections import Counter, defaultdict
from datetime import datetime

def analyze_logs(log_file, report_file):
    os.makedirs(os.path.dirname(report_file), exist_ok=True)
    
    events = []
    with open(log_file) as f:
        for line in f:
            ts, module, sev, code, msg = line.strip().split(" | ")
            events.append({"timestamp": ts, "module": module, "severity": sev, "code": code, "message": msg})
    
    # Count severity
    severity_counts = Counter([e["severity"] for e in events])
    
    # Count by module per severity
    module_counts = defaultdict(lambda: Counter())
    for e in events:
        module_counts[e["module"]][e["severity"]] += 1
    
    # Hourly trend
    hourly_counts = defaultdict(lambda: Counter())
    for e in events:
        hour = datetime.strptime(e["timestamp"], "%Y-%m-%d %H:%M:%S").hour
        hourly_counts[hour][e["severity"]] += 1
    
    # Detect anomalies
    anomalies = []
    if severity_counts["ERROR"] > 40:
        anomalies.append(f"High error volume detected ({severity_counts['ERROR']} errors)")
    if severity_counts["WARNING"] > 70:
        anomalies.append(f"Warning rate elevated ({severity_counts['WARNING']} warnings)")
    top_error_modules = [m for m, c in module_counts.items() if c["ERROR"] > 0]
    
    # Write report
    with open(report_file, "w") as f:
        f.write("SYSTEM LOG ANALYSIS REPORT\n")
        f.write("===========================\n\n")
        f.write("Event Counts:\n")
        for sev in ["INFO", "WARNING", "ERROR"]:
            f.write(f"  {sev}: {severity_counts.get(sev,0)}\n")
        f.write("\nDetected Anomalies:\n")
        if anomalies:
            for a in anomalies:
                f.write(f"  - {a}\n")
        else:
            f.write("  None\n")
        f.write("\nTop Modules Generating Errors:\n")
        for m in top_error_modules:
            f.write(f"  - {m} ({module_counts[m]['ERROR']} errors)\n")
        f.write("\nHourly Event Trend:\n")
        for hour in sorted(hourly_counts.keys()):
            counts = hourly_counts[hour]
            f.write(f"  Hour {hour}: INFO={counts.get('INFO',0)}, WARNING={counts.get('WARNING',0)}, ERROR={counts.get('ERROR',0)}\n")
