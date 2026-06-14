import schedule
import time
import subprocess

def run_reports():
    print("Generating Charts...")
    subprocess.run(["python", "scripts/generate_charts.py"])

    print("Generating PDF...")
    subprocess.run(["python", "scripts/generate_pdf_report.py"])

    print("Exporting CSV...")
    subprocess.run(["python", "scripts/export_report.py"])

    print("Sending Email...")
    subprocess.run(["python", "scripts/email_alert.py"])

    print("Task Completed!")

# Testing
schedule.every(10).seconds.do(run_reports)

print("Scheduler Started...")

while True:
    schedule.run_pending()
    time.sleep(1)