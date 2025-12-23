[![CI](https://github.com/DanielJamesDev/LogAnomalyDetector/actions/workflows/ci.yml/badge.svg)](https://github.com/DanielJamesDev/LogAnomalyDetector/actions/workflows/ci.yml)



# Log Anomaly Detector - System Log Analysis & Anomaly Detection

## Overview
This project demonstrates realistic system log generation, parsing, analysis, and anomaly detection. It simulates an operational system producing hundreds of log events, quantifies error/warning events, detects anomalies, and produces a professional summary report. The repository reflects workflows used in production environments for software and systems engineering roles.

## Features
- Generates realistic system logs (INFO, WARNING, ERROR)
- Parses timestamps, severity levels, and messages
- Counts and analyzes events, detecting anomalies
- Produces professional summary reports
- Automated unit tests with pytest
- Cross-platform, reproducible execution

## Skills Highlighted
- Python programming and modular design
- Data parsing, statistical analysis, and anomaly detection
- Test-driven development
- Linux and cross-platform workflow
- System diagnostics and monitoring

## Getting Started

### Prerequisites
- Python 3.10+
- Dependencies listed in `requirements.txt`

### Installation
```bash
git clone https://github.com/YourUsername/LogAnomalyDetector.git
cd LogAnomalyDetector
pip install -r requirements.txt
```
### Run Demo
```bash
python -m src.demo
```
### This will generate:
- `logs/system.log` (auto-generated system log with hundreds of events)
- `outputs/summary_report.txt` (analysis report highlighting event counts and detected anomalies)

### Run Tests
```bash
pytest
```

### Project Structure

- `src/` - source modules and demo script
- `logs` - auto-generated log files
- `outputs` - generated summary reports
- `tests` - unit tests
- `requirements.txt` - Python dependencies
- `README.md` - project documentation

### Author
**Daniel J. Farley**
Programmer / Analyst | Portfolio Artifact
[dfarley78@gmail.com](mailto:dfarley78@gmail.com)

