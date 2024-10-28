#!/bin/python3
"""
script that reads stdin line by line
"""
import sys
import re
from collections import defaultdict

# Define components of the regex for clarity
ip_pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
date_pattern = r'(?P<date>.+?)'
status_pattern = r'(?P<status>\d{3})'
size_pattern = r'(?P<size>\d+)'

# Combine the components into a single regex
log_pattern = re.compile(
    rf'^{ip_pattern} - \['
    rf'{date_pattern}\] "GET /projects/260 HTTP/1.1" '
    rf'{status_pattern} {size_pattern}$'
)

# Function to process a single log line
def process_log_line(line):
    match = log_pattern.match(line)
    if match:
        return {
            "ip": match.group("ip"),
            "date": match.group("date"),
            "status": match.group("status"),
            "size": int(match.group("size"))
        }
    return None

# Function to print metrics
def print_metrics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status in sorted(status_counts):
        print(f"{status}: {status_counts[status]}")

def main():
    # Initialize variables to store metrics
    total_file_size = 0
    status_codes_count = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            # Process the log line
            result = process_log_line(line)
            if result:  # If the line is valid
                total_file_size += result["size"]
                status_codes_count[result["status"]] += 1
                line_count += 1
                
                # Every 10 lines or on keyboard interruption, print metrics
                if line_count % 10 == 0:
                    print_metrics(total_file_size, status_codes_count)
        
    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully
        print_metrics(total_file_size, status_codes_count)

if __name__ == "__main__":
    main()
