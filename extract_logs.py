import sys
import os
from datetime import datetime

def estimate_position(file_size, target_date, start_date, end_date):
    """Estimate the position in the file for the target date."""
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    target_date = datetime.strptime(target_date, "%Y-%m-%d")

    total_days = (end_date - start_date).days
    target_day = (target_date - start_date).days

    return int((target_day / total_days) * file_size)

def extract_logs(file_path, target_date, output_dir):
    """Extract logs for the specified date."""
    start_date = "2024-01-01"
    end_date = "2024-12-31"

    file_size = os.path.getsize(file_path)
    estimated_position = estimate_position(file_size, target_date, start_date, end_date)

    logs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        file.seek(estimated_position)
        
        # Move to the start of the next line
        file.readline()
        
        # Read lines until we find the target date
        for line in file:
            log_date = line.split('T')[0]
            if log_date == target_date:
                logs.append(line)
            elif logs and log_date != target_date:
                break

    # Write logs to output file
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(logs)

    print(f"Logs for {target_date} have been saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    target_date = sys.argv[1]
    log_file = "large_log_file.txt"  # Replace with the actual path to the log file
    output_dir = "output"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    extract_logs(log_file, target_date, output_dir)
