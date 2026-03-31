from datetime import datetime
import os

def log_event(message, logfile="output/logs/forensic_log.txt"):

    # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(logfile), exist_ok=True)

    with open(logfile, "a") as log:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{time}] {message}\n")