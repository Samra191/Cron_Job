import schedule
import time
import subprocess

# Path to your script that you want to run
script_path = 'Utoday_website.py'  # Replace with your script's path

# Function to run the script
def run_script():
    subprocess.run(['python', script_path], check=True)  # Runs the script using Python

# Schedule the script to run every Sunday at midnight
schedule.every().sunday.at("00:00").do(run_script)

# Keep the script running to check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute for pending jobs

