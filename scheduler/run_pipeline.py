import os
from datetime import datetime

log_file = "scheduler/log.txt"

with open(log_file, "a") as f:
    f.write(f"\nRun started at {datetime.now()}\n")

os.system("python data_ingestion/generate_data.py")
os.system("python database/db_loader.py")
os.system("python data_processing/process_data.py")

with open(log_file, "a") as f:
    f.write(f"Run completed at {datetime.now()}\n")
