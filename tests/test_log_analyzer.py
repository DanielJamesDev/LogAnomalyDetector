import os
from src.log_generator import generate_logs
from src.log_analyzer import analyze_logs

def test_log_analyzer_creates_report(tmp_path):
    log_file = tmp_path / "system.log"
    report_file = tmp_path / "summary_report.txt"
    generate_logs(str(log_file), num_events=50)
    analyze_logs(str(log_file), str(report_file))
    assert report_file.exists()
