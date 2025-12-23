from src.log_generator import generate_logs
from src.log_analyzer import analyze_logs

LOG_FILE = "logs/system.log"
REPORT_FILE = "outputs/summary_report.txt"

# Generate realistic logs
generate_logs(LOG_FILE, num_events=500)

# Analyze logs and generate report
analyze_logs(LOG_FILE, REPORT_FILE)

print(f"Log analysis complete.\nReport saved to {REPORT_FILE}")
